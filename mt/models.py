#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
import sys

from django.contrib.auth.models import User, Group
from django.db import models

from .util import ProductInformation


class Person(models.Model):
    name = models.CharField(max_length=64)
    director = models.BooleanField(default=False)
    actor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Asset(models.Model):
    """
    Movie Asset model.
    """
    upc = models.CharField(max_length=12, blank=True)

    asin = models.CharField(max_length=24, blank=True, null=True)
    # actors = models.ManyToManyField(Person, related_name="ActorsRelated")
    binding = models.CharField(max_length=64, blank=True, null=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    currency = models.CharField(max_length=24, blank=True, null=True)
    # directors = models.ManyToManyField(Person, related_name="DirectorsRelated")
    features = models.CharField(max_length=512, blank=True, null=True)
    genre = models.ForeignKey(Genre, null=True)
    large_img = models.URLField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    medium_img = models.URLField(blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    sales_rank = models.IntegerField(blank=True, null=True)
    small_img = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=256, blank=False)
    url = models.URLField(blank=True, null=True)

    # editorial_reviews = response.editorial_reviews

    added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True)

    api_fields = ['list_price', 'features', 'binding', 'sales_rank', 'asin', 'title', 'brand', \
                  'price', 'publication_date', 'medium_img', 'url', 'release_date', 'large_img',
                  'small_img', 'model', 'currency']

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.upc)

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        super(Asset, self).save(*args, **kwargs)

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

    def get_product_info(self, save_info=True):
        p = ProductInformation(self.upc)
        for k in self.api_fields:
            if k in p.__dict__:
                # print("Storing: %s" % p.__dict__[k])
                # print(k)
                # print(p.__dict__[k])
                # print(type(p.__dict__[k]))
                self.__dict__[k] = p.__dict__[k]

        if "genre" in p.__dict__:
            name = p.__dict__["genre"]
            if name is not None:
                ng, created = Genre.objects.get_or_create(name=name)
                self.genre = ng
                self.save()
                if created:
                    print("New genre added %s" % ng)
                else:
                    print("Existing genre noted %s" % ng)
            else:
                print("No genre recorded for %s" % self)

        if "actors" in p.__dict__:
            for a in p.__dict__["actors"]:
                np, created = Person.objects.get_or_create(name=a)
                np.actor = True
                np.save()

                if created:
                    print("New person created for actor %s" % np)
                else:
                    print("Updated existing person as actor %s" % np)

        if "directors" in p.__dict__:
            for a in p.__dict__["directors"]:
                np, created = Person.objects.get_or_create(name=a)
                np.director = True
                np.save()

                if created:
                    print("New person created for director %s" % np)
                else:
                    print("Updated existing person as director %s" % np)

        if save_info is True:
            self.save()

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


