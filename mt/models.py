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

    def transaction(self, transaction_type):
        """
        Create a transaction record for this asset.

        :type transaction_type: AssetTransaction
        """
        return AssetTransaction.objects.create(asset=self, trans=transaction_type)

    def add_to_inventory(self):
        return self.transaction(AssetTransaction.TRANSACTION_ADD)

    def checkout(self):
        return self.transaction(AssetTransaction.TRANSACTION_CHECKOUT)

    def loan(self, name=None):
        tr = self.transaction(AssetTransaction.TRANSACTION_CHECKOUT_LOAN)
        tr.note = "Checked out to " + name
        tr.save()
        return(tr)

    def set_unknown(self):
        return self.transaction(AssetTransaction.TRANSACTION_UNKNOWN)

    def remove(self):
        return self.transaction(AssetTransaction.TRANSACTION_REM)

    @property
    def status(self):
        x = AssetTransaction.objects.all().filter(asset=self)
        if len(x) == 0:
            code, description = AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.TRANSACTION_UNKNOWN]

        else:
            code, description = AssetTransaction.TRANSACTION_CHOICES[x[len(x)].trans]

        return description

class AssetTransaction(models.Model):
    """
    AssetTransaction model.
    """
    TRANSACTION_ADD='add'
    TRANSACTION_CHECKOUT='co'
    TRANSACTION_CHECKOUT_LOAN='col'
    TRANSACTION_UNKNOWN='unk'
    TRANSACTION_REM='rem'
    TRANSACTION_CHOICES = ((TRANSACTION_ADD, 'In Inventory'),
                           (TRANSACTION_CHECKOUT, 'Checked Out'),
                           (TRANSACTION_CHECKOUT_LOAN, 'Loaned'),
                           (TRANSACTION_UNKNOWN, 'Unknown'),
                           (TRANSACTION_REM, 'Removed from Inventory Permanently'))
    asset = models.ForeignKey(MovieAsset)
    trans = models.CharField(max_length=3, choices=TRANSACTION_CHOICES, default=TRANSACTION_ADD)
    note = models.CharField(max_length=256, blank=True)
    ts = models.DateTimeField(auto_now_add=True)