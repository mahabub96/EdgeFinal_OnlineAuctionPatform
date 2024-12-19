from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import Log
from django.contrib.auth.models import User

# Log user login action
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    Log.objects.create(
        user=user,
        action="User Logged In",
        details="User logged in successfully."
    )

# Log user logout action
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    Log.objects.create(
        user=user,
        action="User Logged Out",
        details="User logged out successfully."
    )

# Example: Log custom actions (e.g., bids)
@receiver(post_save, sender=User)  # Replace `User` with the relevant model for custom actions
def log_custom_action(sender, instance, created, **kwargs):
    if created:
        Log.objects.create(
            user=instance,
            action="Custom Action",
            details="Description of the action."
        )
