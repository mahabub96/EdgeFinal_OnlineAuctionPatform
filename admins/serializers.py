from rest_framework import serializers
from users.models import User
from auction_items.models import AuctionItem
from categories.models import Category
from .models import AdminLog, AdminNotification

class AdminOverviewSerializer(serializers.Serializer):
    active_auctions = serializers.IntegerField()
    total_users = serializers.IntegerField()
    total_payments = serializers.DecimalField(max_digits=10, decimal_places=2)

class AuctionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLog
        fields = '__all__'

class AdminNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNotification
        fields = '__all__'
