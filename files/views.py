from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from auction_items.models import AuctionItem

class FileListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        files = File.objects.filter(auction_item_id=item_id)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

class FileUploadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, file_id):
        file = get_object_or_404(File, id=file_id, user=request.user)
        file.file_path.delete()  # Delete the file from the storage
        file.delete()  # Delete the file object from the database
        return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@login_required
def file_list(request):
    auction_items = AuctionItem.objects.all()
    return render(request, 'files/list.html', {'auction_items': auction_items})
