from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)  # User email (unique)
    password = models.CharField(max_length=255)  # Password (hashed by Django auth system)
    is_active = models.BooleanField(default=True)  # Account status
    date_joined = models.DateTimeField(auto_now_add=True)  # Date account created
    role_name = models.CharField(max_length=100)  # Role of user (e.g., Admin, Seller)
    permissions = models.JSONField(default=dict)  # Permissions for the user in JSON format

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid clash with default `auth.User.groups`
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Avoid clash with default `auth.User.user_permissions`
        blank=True,
    )

    def __str__(self):
        return self.username


# User Profiles Table
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User
    first_name = models.CharField(max_length=100)  # User's first name
    last_name = models.CharField(max_length=100)  # User's last name
    address = models.TextField()  # User's address
    phone_number = models.CharField(max_length=15)  # User's phone number
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Profile picture

    def __str__(self):
        return self.user.username
