from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.categoryName

class Bid(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bids")

    def __str__(self):
        return str(self.bid)

class Listing(models.Model):
    title = models.CharField(max_length=255)  # Reduced length for optimization
    description = models.TextField(max_length=500)  # Use TextField for longer content
    imageUrl = models.URLField(max_length=200, blank=True, null=True)  # Use URLField for URLs
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="listings")
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="listings")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="listings")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author.username if self.author else 'Anonymous'} comment on {self.listing.title}"


