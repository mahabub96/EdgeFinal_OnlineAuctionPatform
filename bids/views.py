from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bid
from .serializers import BidSerializer

# Fetch user's bid history
class UserBidHistoryAPIView(APIView):
    def get(self, request, user_id):
        bids = Bid.objects.filter(user_id=user_id).order_by('-bid_time')
        if not bids.exists():
            return Response({'message': 'No bids found for this user'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data)


def bid_history(request, user_id):
    bids = Bid.objects.filter(user_id=user_id).order_by('-bid_time')
    return render(request, 'bids/bid_history.html', {'bids': bids})
