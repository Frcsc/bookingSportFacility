from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from users.validations import PASSWORD_REGEX_VALIDATOR

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(validators=[PASSWORD_REGEX_VALIDATOR])

    def validate(self, data):
        email = data['email']
        password = data['password']

        if authenticate(email=email, password=password) is None:
            raise serializers.ValidationError('Invalid credentials')
        return authenticate(email=email, password=password)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
