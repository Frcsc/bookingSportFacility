import datetime
import secrets
import string

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags

from kansala_sports.mixin import BaseModel

password_reset_token = PasswordResetTokenGenerator()


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def send_reset_password_link(self):
        data = {
            'PASSWORD_RESET_PAGE_URL': settings.PASSWORD_RESET_PAGE_URL,
            'token': password_reset_token.make_token(self),
            'email': self.email,
        }
        html_message = render_to_string('password_reset.html', context=data)
        message = EmailMultiAlternatives(
            subject="Reset Password",
            body=strip_tags(html_message),
            to=[self.email],
        )
        message.attach_alternative(html_message, 'text/html')
        message.send()


class TwoFactorAuthentication(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=128)

    def set_new_code(self):
        digits = string.digits
        self.code = ""

        self.code = ''.join(secrets.choice(digits) for i in range(6))
        return self.code

    def send_two_factor_code_email(self, name):
        data = {'code': self.code, 'name': name, 'email': self.user.email}
        html_message = render_to_string('user_confirmation_code.html', context=data)
        message = EmailMultiAlternatives(
            subject="Security Code",
            body=strip_tags(html_message),
            to=[self.user.email],
        )
        message.attach_alternative(html_message, 'text/html')
        message.send()

    def code_has_expired(self, code):
        now = timezone.now()
        code_expiration_time = self.updated_at + datetime.timedelta(minutes=5)
        return self.code == code and now > code_expiration_time
