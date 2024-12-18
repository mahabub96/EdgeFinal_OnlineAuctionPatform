from django.contrib import admin
from .models import AdminLog, AdminNotification

@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "timestamp")

@admin.register(AdminNotification)
class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created_at", "is_read")
