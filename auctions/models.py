from django.db import models


class Auction(models.Model):
    auc_id = models.IntegerField(default=None)
    item_id = models.IntegerField(default=None)
    realm = models.CharField(max_length=20)
    bid = models.IntegerField(default=None)
    buyout = models.IntegerField(default=None)
    quantity = models.IntegerField(default=None)
    time_left = models.CharField(max_length=20)

    def __str__(self):
        return 'Auction nr: ' + str(self.auc_id)
