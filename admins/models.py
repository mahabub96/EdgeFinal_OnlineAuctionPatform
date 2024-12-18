from django.db import models
from users.models import User

class AdminLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Log by {self.user.username}: {self.action}"

class AdminNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"