# Create your models here.
from django.db import models
from users.models import User  # Import User model

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  # User (Foreign Key)
    message = models.TextField()  # Notification message
    is_read = models.BooleanField(default=False)  # Whether the notification is read or not
    event_type = models.CharField(max_length=100)  # Type of event triggering the notification
    created_at = models.DateTimeField(auto_now_add=True)  # Date the notification was created
    send_email = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.event_type}"
