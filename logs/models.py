# Create your models here.
from django.db import models
from users.models import User  # Import User model

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')  # User (Foreign Key)
    action = models.CharField(max_length=100)  # Action description
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the action
    details = models.TextField()  # Additional details about the action

    def __str__(self):
        return f"Log for {self.user.username} - {self.action}"
