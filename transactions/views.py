from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from django.shortcuts import render

class UserTransactionHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if request.user.id != user_id:
            return Response({"error": "You are not authorized to view this user's transactions."}, status=403)

        transactions = Transaction.objects.filter(user_id=user_id).order_by('-created_at')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

def transaction_history(request):
    return render(request, 'transactions/history.html')