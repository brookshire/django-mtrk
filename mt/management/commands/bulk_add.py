#
#  bulk_add.py
#
#

import time

from django.contrib.auth.models import User

from amazon.api import AsinNotFound
from django.core.management.base import BaseCommand

from mt.models import Asset
from mt.models import AssetTransaction

delay = 1

class Command(BaseCommand):
    help = "Bulk add assests to the database"

    def add_arguments(self, parser):
        parser.add_argument("input_files", nargs='+', type=str)

    def handle(self, *args, **options):
        u = User.objects.all()[0]
        for fname in options["input_files"]:
            print("Loading SKUs from %s" % fname)
            fp = open(fname, "r")

            loaded = []
            failed = []

            for upc in fp.readlines():
                upc = upc.strip()
                # print("Loading asset data for %s" % upc)
                na, created = Asset.objects.get_or_create(upc=upc)
                na.created_by = u
                na.save()

                try:
                    na.get_product_info()

                    if created:
                        print("Added asset %s to database" % na)
                    else:
                        print("Updated asset %s in database" % na)

                    loaded.append(upc)

                    # print("===>>>> %s" % na.status_str)
                    if na.status != AssetTransaction.CHECK_IN:
                        nt = AssetTransaction.objects.create(asset=na,
                                                             user=u,
                                                             trans=AssetTransaction.CHECK_IN,
                                                             note="Added by bulk_add command")
                        print("Checked %s into inventory" % na)
                    else:
                        print("%s already checked into inventory" % na)

                except AsinNotFound:
                    na.delete()
                    failed.append(upc)
                    print("Failed to load product information for UPC %s" % upc)

                time.sleep(delay)

            fp.close()