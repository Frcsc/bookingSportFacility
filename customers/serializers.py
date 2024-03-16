from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from customers.models import CustomerProfile
from users.serializers import UserSerializer
from users.validations import PASSWORD_REGEX_VALIDATOR

User = get_user_model()


class RegisterCustomerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(validators=[PASSWORD_REGEX_VALIDATOR])

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email belongs to another user")
        return email

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        name = validated_data.get('name')

        user = User.objects.create_user(email=email, password=password)
        customer = CustomerProfile.objects.create(user=user, name=name)

        return customer


class CustomerTwoFactorVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "You cannot verify an account that does not exist"
            )
        if User.objects.filter(email=value, is_verified=True).exists():
            raise serializers.ValidationError("This account has already been verified")
        return value


class CustomerRequestNewVerficationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "You cannot verify an account that does not exist"
            )
        if User.objects.filter(email=value, is_verified=True).exists():
            raise serializers.ValidationError("This account has already been verified")
        return value


class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(validators=[PASSWORD_REGEX_VALIDATOR])

    def validate(self, data):
        email = data['email']
        password = data['password']

        if authenticate(email=email, password=password) is None:
            raise serializers.ValidationError('Invalid credentials')
        return authenticate(email=email, password=password)


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['id', 'name', 'user']

    user = UserSerializer()
