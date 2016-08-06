#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.db import models

class MovieAsset(models.Model):
    """
    Movie Asset model.
    """
    barcode = models.CharField(max_length=12, blank=True)
    title = models.CharField(max_length=256, blank=False)
    list_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    image_url_sm = models.URLField(blank=True)
    image_url_med = models.URLField(blank=True)
    image_url_lg = models.URLField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title + " (" + self.barcode + ")"

    @property
    def status(self):
        records = AssetTransaction.objects.all()
        if len(records) > 0:
            return records[0].trans
        else:
            return AssetTransaction.UNKNOWN

    @property
    def status_str(self):
        idx, desc = AssetTransaction.TRANSACTION_CHOICES[self.status]
        return desc

class AssetTransaction(models.Model):
    """
    AssetTransaction model.
    """
    UNKNOWN = 0
    CHECK_IN = 1
    CHECK_OUT = 2
    LOAD = 3
    REMOVED = 4

    TRANSACTION_CHOICES = (
        (CHECK_IN, 'In Inventory'),
        (CHECK_OUT, 'Checked Out'),
        (LOAD, 'Loaned'),
        (UNKNOWN, 'Unknown'),
        (REMOVED, 'Removed from Inventory Permanently'))
    asset = models.ForeignKey(MovieAsset)
    trans = models.IntegerField(choices=TRANSACTION_CHOICES, default=CHECK_IN)
    note = models.CharField(max_length=256, blank=True)
    ts = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        idx, desc = self.TRANSACTION_CHOICES[self.trans]
        return "%s: %s" % (self.asset, desc)
