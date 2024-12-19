from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Notification

@receiver(post_save, sender=Notification)
def send_email_notification(sender, instance, created, **kwargs):
    if created and instance.send_email:
        send_mail(
            subject=f"New Notification: {instance.event_type}",
            message=instance.message,
            from_email='your-email@gmail.com',  # Update this
            recipient_list=[instance.user.email],
            fail_silently=False,
        )
