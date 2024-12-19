from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Log
from .serializers import LogSerializer

# Logs List API View
class UserLogsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if request.user.id != user_id:
            return Response({'error': 'Unauthorized access'}, status=403)
        
        logs = Log.objects.filter(user_id=user_id).order_by('-timestamp')
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

# Logs List Template View
@login_required
def logs_list(request):
    logs = Log.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'logs/list.html', {'logs': logs})
