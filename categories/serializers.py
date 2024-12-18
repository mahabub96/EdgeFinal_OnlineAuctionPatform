from rest_framework import serializers
from .models import Category
from auction_items.models import AuctionItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class AuctionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = ['id', 'title', 'starting_price', 'current_price', 'end_date']
