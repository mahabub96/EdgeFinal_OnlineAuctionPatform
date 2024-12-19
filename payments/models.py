# Create your models here.
from django.db import models
from users.models import User  # Import User model
from auction_items.models import AuctionItem  # Import AuctionItem model

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')  # User (Foreign Key)
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, related_name='payments')  # Auction item (Foreign Key)
    payment_status = models.CharField(max_length=20)  # Payment status (e.g., "Pending", "Completed")
    transaction_id = models.CharField(max_length=255)  # Unique transaction identifier
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount
    payment_date = models.DateTimeField(auto_now_add=True)  # Payment date

    def __str__(self):
        return f"Payment of {self.amount} for {self.auction_item.title}"
