# Create your models here.
from django.db import models
from users.models import User  # Import User model
from auction_items.models import AuctionItem  # Import AuctionItem model

class Transaction(models.Model):
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, related_name='transactions')  # Auction item (Foreign Key)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')  # User (Foreign Key)
    transaction_type = models.CharField(max_length=50)  # Transaction type (e.g., "purchase", "refund")
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    created_at = models.DateTimeField(auto_now_add=True)  # Date of transaction

    def __str__(self):
        return f"{self.transaction_type} for {self.amount} on {self.auction_item.title}"
