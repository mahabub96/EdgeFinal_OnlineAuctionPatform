# Register your models here.
from django.contrib import admin
from .models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role_name', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'role_name')
    list_filter = ('is_active', 'date_joined')
    ordering = ('-date_joined',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'phone_number')


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
