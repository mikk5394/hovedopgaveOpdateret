from django.db import models


class Auction(models.Model):

    item = models.IntegerField(default=0, primary_key=True)
    bid = models.IntegerField(default=0)
    buyout = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    time_left = models.CharField(max_length=50)

