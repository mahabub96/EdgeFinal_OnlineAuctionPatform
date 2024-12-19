from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer
from paypalrestsdk import Payment as PayPalPayment
import paypalrestsdk

# Initialize PayPal SDK (Replace with your credentials)
paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET",
})


# Initiate Payment
class PaymentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            payment_data = serializer.validated_data
            # Create PayPal Payment
            paypal_payment = PayPalPayment({
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "redirect_urls": {
                    "return_url": "http://localhost:8000/payments/success/",
                    "cancel_url": "http://localhost:8000/payments/cancel/",
                },
                "transactions": [{
                    "item_list": {
                        "items": [{
                            "name": "Auction Item",
                            "sku": "auction_item",
                            "price": str(payment_data['amount']),
                            "currency": "USD",
                            "quantity": 1,
                        }]
                    },
                    "amount": {
                        "total": str(payment_data['amount']),
                        "currency": "USD",
                    },
                    "description": f"Payment for auction item: {payment_data['auction_item']}",
                }]
            })

            if paypal_payment.create():
                # Save payment with "Pending" status
                Payment.objects.create(
                    user=request.user,
                    auction_item=payment_data['auction_item'],
                    payment_status="Pending",
                    amount=payment_data['amount'],
                    transaction_id=paypal_payment.id
                )
                # Redirect to PayPal payment URL
                for link in paypal_payment.links:
                    if link.rel == "approval_url":
                        return Response({"approval_url": link.href}, status=status.HTTP_200_OK)
            return Response({"error": "PayPal payment creation failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Payment Status
class PaymentStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Payment History
class PaymentHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        payments = Payment.objects.filter(user_id=user_id)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Template Rendering for Payment Pages
class PaymentPageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'payments/payment.html')


class PaymentHistoryPageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_payments = Payment.objects.filter(user=request.user)
        return render(request, 'payments/history.html', {'payments': user_payments})
