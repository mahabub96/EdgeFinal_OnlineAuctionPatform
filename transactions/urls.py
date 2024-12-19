from django.urls import path
from . import views

urlpatterns = [
    path('api/transactions/user/<int:user_id>/', views.UserTransactionHistoryAPIView.as_view(), name='user_transaction_history_api'),
    path('transactions/history/', views.transaction_history, name='transaction_history'),
]