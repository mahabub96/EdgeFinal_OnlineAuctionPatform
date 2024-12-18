from django.urls import path
from .views import CategoryListAPIView, CategoryItemsAPIView, category_list

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='category_list_api'),
    path('api/categories/<int:category_id>/items/', CategoryItemsAPIView.as_view(), name='category_items'),
    path('categories/', category_list, name='category_list'),  # HTML rendering
]
