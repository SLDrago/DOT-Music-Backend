from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user

class EditUserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)  # For setting new password

    class Meta:
        model = User
        fields = ['name', 'email', 'birthday', 'gender', 'new_password']

    def validate(self, data):
        # Validate new password if provided
        if 'new_password' in data:
            validate_password(data['new_password'], self.instance)  # Validate new password
        return data

    def update(self, instance, validated_data):
        # Update the password if it's provided
        if 'new_password' in validated_data:
            instance.set_password(validated_data['new_password'])
            validated_data.pop('new_password')  # Remove new_password from validated_data

        return super().update(instance, validated_data)