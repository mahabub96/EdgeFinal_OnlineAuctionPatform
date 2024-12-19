from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(LoginRequiredMixin, APIView):
    def get(self, request, user_id):
        if request.user.id != user_id:
            return Response({"error": "You are not authorized to view these notifications."}, status=status.HTTP_403_FORBIDDEN)
        
        notifications = Notification.objects.filter(user_id=user_id)
        serializer = NotificationSerializer(notifications, many=True)
        
        return Response(serializer.data)

    def patch(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        if request.user != notification.user:
            return Response({"error": "You are not authorized to update this notification."}, status=status.HTTP_403_FORBIDDEN)
        
        notification.is_read = True
        notification.save()
        return Response({"message": "Notification marked as read."})

def notification_list_template(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notifications/list.html', {'notifications': notifications})
