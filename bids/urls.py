from django.urls import path
from .views import UserBidHistoryAPIView, bid_history

urlpatterns = [
    path('api/bids/user/<int:user_id>/', UserBidHistoryAPIView.as_view(), name='user_bid_history_api'),
    path('bids/user/<int:user_id>/', bid_history, name='user_bid_history'),  # For template rendering
]
