#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.db import models
from django.contrib.auth.models import User, Group
from .util import ProductInformation

class Person(models.Model):
    name = models.CharField(max_length=64)

class Genre(models.Model):
    name = models.CharField(max_length=64)

class Asset(models.Model):
    """
    Movie Asset model.
    """
    upc = models.CharField(max_length=12, blank=True)
    asin = models.CharField(max_length=24, blank=True)

    title = models.CharField(max_length=256, blank=False)
    list_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    small_img = models.URLField(blank=True)
    medium_img = models.URLField(blank=True)
    large_img = models.URLField(blank=True)
    actors = models.ManyToManyField(Person, related_name="ActorsRelated")
    directors = models.ManyToManyField(Person, related_name="DirectorsRelated")
    model = models.CharField(max_length=64, blank=True)
    binding = models.CharField(max_length=64, blank=True)
    brand = models.CharField(max_length=64, blank=True)
    genre = models.ForeignKey(Genre, null=True)
    features = models.CharField(max_length=64, blank=True)
    url = models.URLField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    sales_rank = models.IntegerField(blank=True, null=True)
    # editorial_reviews = response.editorial_reviews

    added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title

    @property
    def status(self):
        """
        Determine the current state of this asset based on transaction records.
        :return: The last transaction's code, or unknown if no transactions have been recorded.
        """
        records = AssetTransaction.objects.all()
        record_count = len(records)
        if record_count > 0:
            return records[record_count-1].trans
        else:
            return AssetTransaction.UNKNOWN

    @property
    def status_str(self):
        idx, desc = AssetTransaction.TRANSACTION_CHOICES[self.status]
        return desc

    def transaction(self, trans, note=None):
        tr = AssetTransaction.objects.create(asset=self,
                                             trans=trans,
                                             note=note)
        return tr

    def check_in(self):
        return self.transaction(AssetTransaction.CHECK_IN)

    def check_out(self):
        return self.transaction(AssetTransaction.CHECK_OUT)

    def loan(self, to):
        return self.transaction(AssetTransaction.LOAN, to)

    def unknown(self):
        return self.transaction(AssetTransaction.UNKNOWN)

    def remove(self):
        return self.transaction(AssetTransaction.REMOVED)



class AssetTransaction(models.Model):
    """
    AssetTransaction model.
    """
    #  Transaction
    UNKNOWN = 0
    CHECK_IN = 1
    CHECK_OUT = 2
    LOAN = 3
    REMOVED = 4

    TRANSACTION_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (CHECK_IN, 'In Inventory'),
        (CHECK_OUT, 'Checked Out'),
        (LOAN, 'Loaned'),
        (REMOVED, 'Removed from Inventory Permanently'))

    asset = models.ForeignKey(Asset)
    trans = models.IntegerField(choices=TRANSACTION_CHOICES, default=UNKNOWN)
    note = models.CharField(max_length=256, blank=True, null=True)
    ts = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        idx, desc = self.TRANSACTION_CHOICES[self.trans]
        return "%s: %s" % (self.asset, desc)


