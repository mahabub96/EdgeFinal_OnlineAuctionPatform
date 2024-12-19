from django.urls import path
from . import views

urlpatterns = [
    path('api/files/auction-item/<int:item_id>/', views.FileListAPIView.as_view(), name='file_list_api'),
    path('api/files/', views.FileUploadAPIView.as_view(), name='file_upload_api'),
    path('api/files/<int:file_id>/', views.FileDeleteAPIView.as_view(), name='file_delete_api'),
    path('files/', views.file_list, name='file_list'),
]