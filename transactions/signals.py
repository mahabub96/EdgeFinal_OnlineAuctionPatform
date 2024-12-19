# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Transaction
# from auction_items.models import AuctionItem

# @receiver(post_save, sender=Transaction)
# def update_after_transaction(sender, instance, created, **kwargs):
#     if created:  # Only trigger on new transactions
#         transaction = instance

#         # Example logic: Mark the auction item as sold after a purchase transaction
#         if transaction.transaction_type == "purchase":
#             auction_item = transaction.auction_item
#             auction_item.is_sold = True
#             auction_item.save()

#         # Add other updates here based on transaction type
#         print(f"Transaction processed: {transaction.transaction_type} for {transaction.amount}")
