#
#  bulk_add.py
#
#

from django.core.management.base import BaseCommand, CommandError
from mt.models import Asset

class Command(BaseCommand):
    help = "Bulk add assests to the database"

    def add_arguments(self, parser):
        parser.add_argument("input_files", nargs='+', type=str)

    def handle(self, *args, **options):
        for fname in options["input_files"]:
            fp = open(fname, "r")
            for upc in fp.readlines():
                na, created = Asset.objects.get_or_create(upc=upc)
                na.get_product_info()

                if created:
                    print("Added asset %s to database" % na)

                else:
                    print("Updated asset %s in database" % na)

                # if created:
                #     print("Found new asset.  Loading product data.")
                #     na.get_product_info()
                # else:
                #     print("Found existing product information.")
