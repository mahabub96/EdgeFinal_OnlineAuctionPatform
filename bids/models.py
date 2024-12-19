# Create your models here.
from django.db import models
from users.models import User  # Import User model
from auction_items.models import AuctionItem  # Import AuctionItem model

class Bid(models.Model):
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, related_name='bids')  # Auction item (Foreign Key)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')  # Bidder (Foreign Key)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Bid amount
    bid_time = models.DateTimeField(auto_now_add=True)  # Bid time

    def __str__(self):
        return f"Bid of {self.bid_amount} by {self.user.username} on {self.auction_item.title}"
