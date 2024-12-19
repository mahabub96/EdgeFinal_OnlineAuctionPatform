# Create your models here.
from django.db import models
from users.models import User  # Import User model
from auction_items.models import AuctionItem  # Import AuctionItem model

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')  # User (Foreign Key)
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, related_name='files')  # Auction item (Foreign Key)
    file_path = models.FileField(upload_to='auction_files/')  # File path for the uploaded file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # File upload timestamp

    def __str__(self):
        return f"File for {self.auction_item.title} by {self.user.username}"
