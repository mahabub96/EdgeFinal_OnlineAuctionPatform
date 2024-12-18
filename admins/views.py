from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from auction_items.models import AuctionItem
from users.models import User
from categories.models import Category
from payments.models import Payment
from .models import AdminLog, AdminNotification
from .serializers import (
    AdminOverviewSerializer, AuctionItemSerializer, UserSerializer,
    CategorySerializer, AdminLogSerializer, AdminNotificationSerializer
)

class AdminOverviewView(APIView):
    def get(self, request):
        data = {
            "active_auctions": AuctionItem.objects.filter(end_date__gt=timezone.now()).count(),
            "total_users": User.objects.count(),
            "total_payments": Payment.objects.aggregate(total=models.Sum('amount'))['total'],
        }
        if request.accepts('text/html'):
            return render(request, 'admins/dashboard.html', context=data)
        serializer = AdminOverviewSerializer(data)
        return Response(serializer.data)

class ManageAuctionsView(APIView):
    def get(self, request):
        auctions = AuctionItem.objects.all()
        if request.accepts('text/html'):
            return render(request, 'admins/manage_items.html', {'auctions': auctions})
        serializer = AuctionItemSerializer(auctions, many=True)
        return Response(serializer.data)

    def patch(self, request, item_id):
        auction = get_object_or_404(AuctionItem, id=item_id)
        serializer = AuctionItemSerializer(auction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManageUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        if request.accepts('text/html'):
            return render(request, 'admins/manage_items.html', {'users': users})
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManageCategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        if request.accepts('text/html'):
            return render(request, 'admins/manage_items.html', {'categories': categories})
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminLogsView(APIView):
    def get(self, request):
        logs = AdminLog.objects.all()
        if request.accepts('text/html'):
            return render(request, 'admins/logs_and_notifications.html', {'logs': logs})
        serializer = AdminLogSerializer(logs, many=True)
        return Response(serializer.data)

class AdminNotificationsView(APIView):
    def get(self, request):
        notifications = AdminNotification.objects.all()
        if request.accepts('text/html'):
            return render(request, 'admins/logs_and_notifications.html', {'notifications': notifications})
        serializer = AdminNotificationSerializer(notifications, many=True)
        return Response(serializer.data)

# from django.shortcuts import render, get_object_or_404
# from django.utils import timezone
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from auction_items.models import AuctionItem
# from users.models import User
# from categories.models import Category
# from payments.models import Payment
# from .models import AdminLog, AdminNotification
# from .serializers import (
#     AdminOverviewSerializer, AuctionItemSerializer, UserSerializer,
#     CategorySerializer, AdminLogSerializer, AdminNotificationSerializer
# )


# # Admin Overview
# class AdminOverviewView(APIView):
#     # """
#     # Provides admin overview data such as active auctions, total users, and total payments.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         data = {
#             "active_auctions": AuctionItem.objects.filter(end_date__gt=timezone.now()).count(),
#             "total_users": User.objects.count(),
#             "total_payments": Payment.objects.aggregate(total=models.Sum('amount'))['total'],
#         }
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/dashboard.html', context=data)
#         # Return JSON response
#         serializer = AdminOverviewSerializer(data)
#         return Response(serializer.data)


# # Manage Auctions
# class ManageAuctionsView(APIView):
#     # """
#     # Handles fetching and partial updating of auction items.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         auctions = AuctionItem.objects.all()
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/manage_items.html', {'auctions': auctions})
#         # Return JSON response
#         serializer = AuctionItemSerializer(auctions, many=True)
#         return Response(serializer.data)

#     def patch(self, request, item_id):
#         auction = get_object_or_404(AuctionItem, id=item_id)
#         serializer = AuctionItemSerializer(auction, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Manage Users
# class ManageUsersView(APIView):
#     # """
#     # Handles fetching and partial updating of users.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         users = User.objects.all()
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/manage_users.html', {'users': users})
#         # Return JSON response
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def patch(self, request, user_id):
#         user = get_object_or_404(User, id=user_id)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Manage Categories
# class ManageCategoriesView(APIView):
#     # """
#     # Handles fetching, creating, updating, and deleting categories.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         categories = Category.objects.all()
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/manage_categories.html', {'categories': categories})
#         # Return JSON response
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, category_id):
#         category = get_object_or_404(Category, id=category_id)
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, category_id):
#         category = get_object_or_404(Category, id=category_id)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Admin Logs
# class AdminLogsView(APIView):
#     # """
#     # Handles fetching admin logs.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         logs = AdminLog.objects.all()
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/logs_and_notifications.html', {'logs': logs})
#         # Return JSON response
#         serializer = AdminLogSerializer(logs, many=True)
#         return Response(serializer.data)


# # Admin Notifications
# class AdminNotificationsView(APIView):
#     # """
#     # Handles fetching admin notifications.
#     # Renders a template or returns JSON data depending on the request type.
#     # """

#     def get(self, request):
#         notifications = AdminNotification.objects.all()
#         # Render template if the request expects HTML
#         if request.accepts('text/html'):
#             return render(request, 'admins/logs_and_notifications.html', {'notifications': notifications})
#         # Return JSON response
#         serializer = AdminNotificationSerializer(notifications, many=True)
#         return Response(serializer.data)


# class AddCategoryView(APIView):
#     def get(self, request):
#         # Render a form for adding a new category
#         return render(request, 'admins/add_category.html')  # You can create a form template here

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)