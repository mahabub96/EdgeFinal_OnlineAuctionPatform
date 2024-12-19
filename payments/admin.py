from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'auction_item', 'amount', 'payment_status', 'transaction_id', 'payment_date']
    search_fields = ['user__username', 'auction_item__title', 'transaction_id']
    list_filter = ['payment_status', 'payment_date']
