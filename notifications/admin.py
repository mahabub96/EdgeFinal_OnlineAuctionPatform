from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'is_read', 'send_email', 'created_at')
    list_filter = ('is_read', 'send_email', 'created_at')
