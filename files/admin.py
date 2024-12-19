from django.contrib import admin
from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction_item', 'file_path', 'uploaded_at')
    search_fields = ('user__username', 'auction_item__title')
    list_filter = ('uploaded_at',)
