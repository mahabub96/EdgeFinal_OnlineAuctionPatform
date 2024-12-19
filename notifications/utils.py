from django.core.mail import send_mail
from .models import Notification

def create_notification(user, message, event_type, send_email=False):
    notification = Notification.objects.create(
        user=user,
        message=message,
        event_type=event_type,
        send_email=send_email,
    )
    
    if send_email:
        send_mail(
            subject=f"New Notification: {event_type}",
            message=message,
            from_email='your-email@gmail.com',
            recipient_list=[user.email],
            fail_silently=False,
        )
    
    return notification


# from notifications.models import Notification

# def create_notification(user, message, event_type, send_email=False):
#     """
#     Utility function to create a notification.
    
#     Args:
#         user (User): The user to whom the notification will be sent.
#         message (str): The notification message.
#         event_type (str): The type of event triggering the notification.
#         send_email (bool): Whether to send an email for this notification.
#     """
#     notification = Notification.objects.create(
#         user=user,
#         message=message,
#         event_type=event_type,
#         send_email=send_email,
#     )
#     return notification
