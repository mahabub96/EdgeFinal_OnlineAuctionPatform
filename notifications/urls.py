from django.urls import path
from .views import NotificationListView, notification_list_template

urlpatterns = [
    path('api/notifications/user/<int:user_id>/', NotificationListView.as_view(), name='api-notification-list'),
    path('api/notifications/<int:notification_id>/', NotificationListView.as_view(), name='api-notification-update'),
    path('notifications/list/', notification_list_template, name='template-notification-list'),
]
