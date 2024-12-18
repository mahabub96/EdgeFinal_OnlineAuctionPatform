from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Category
from auction_items.models import AuctionItem
from .serializers import CategorySerializer, AuctionItemSerializer

# List all categories
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Fetch items under a specific category
class CategoryItemsAPIView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        auction_items = AuctionItem.objects.filter(category=category)
        serializer = AuctionItemSerializer(auction_items, many=True)
        return Response(serializer.data)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

