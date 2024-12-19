from django.contrib import admin
from .models import Bid

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['auction_item', 'user', 'bid_amount', 'bid_time']
    list_filter = ['bid_time', 'auction_item']
    search_fields = ['user__username', 'auction_item__title']
