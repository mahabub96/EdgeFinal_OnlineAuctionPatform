from rest_framework import serializers
from .models import Bid
from auction_items.models import AuctionItem

class AuctionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = ['id', 'title', 'current_price', 'end_date']

class BidSerializer(serializers.ModelSerializer):
    auction_item = AuctionItemSerializer()  # Nesting AuctionItem details

    class Meta:
        model = Bid
        fields = ['id', 'auction_item', 'bid_amount', 'bid_time']
