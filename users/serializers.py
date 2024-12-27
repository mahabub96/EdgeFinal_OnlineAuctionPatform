from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomClaimTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom claims to the token response
        data['role_name'] = self.user.role_name  # Add the user's role
        data['permissions'] = self.user.permissions  # Add the user's permissions
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role_name', 'permissions', 'is_active']
        read_only_fields = ['id', 'is_active']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'profile_picture']


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    role_name = serializers.ChoiceField(choices=User.ROLE_CHOICES, write_only=True)  # Enforce choices validation

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role_name=validated_data['role_name'],  # Assign role_name
        )
        return user



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    uid = serializers.IntegerField()
    new_password = serializers.CharField()

    def validate_new_password(self, value):
        validate_password(value)
        return value
