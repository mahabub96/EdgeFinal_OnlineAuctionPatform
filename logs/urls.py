from django.urls import path
from . import views

urlpatterns = [
    # API endpoint
    path('api/logs/user/<int:user_id>/', views.UserLogsAPIView.as_view(), name='user_logs_api'),
    
    # Logs list page
    path('logs/', views.logs_list, name='logs_list'),
]
