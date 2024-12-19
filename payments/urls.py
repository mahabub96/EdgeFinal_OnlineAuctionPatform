from django.urls import path
from .views import PaymentCreateView, PaymentStatusView, PaymentHistoryView, PaymentPageView, PaymentHistoryPageView

urlpatterns = [
    path('api/payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('api/payments/status/<int:payment_id>/', PaymentStatusView.as_view(), name='payment-status'),
    path('api/payments/user/<int:user_id>/', PaymentHistoryView.as_view(), name='payment-history'),
    path('payments/', PaymentPageView.as_view(), name='payment-page'),
    path('payments/history/', PaymentHistoryPageView.as_view(), name='payment-history-page'),
]
