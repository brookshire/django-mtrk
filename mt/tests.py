#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.test import TestCase

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .models import MovieAsset, AssetTransaction
from .views import home_page

class MovieAssetTests(TestCase):
    def setUp(self):
        self.assets = []
        self.assets.append(MovieAsset.objects.create(title="FooBar Baz in America",
                                                     barcode="123456789012"))

    def test_default_instance_creation(self):
        for a in self.assets:
            self.assertEqual(a.title, "FooBar Baz in America")
            self.assertEqual(str(a), "FooBar Baz in America (123456789012)")

    def test_default_asset_transaction(self):
        idx, default_trans_str = AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_IN]

        for a in self.assets:
            tr = AssetTransaction.objects.create(asset=a, trans=AssetTransaction.CHECK_IN)
            print("%s is %s" % (a, a.status))
            self.assertEqual(AssetTransaction.CHECK_IN, a.status)
            self.assertEqual(default_trans_str, a.status_str)

    def test_site_home_content(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # self.assertEqual(response.content.decode(),
        #                  expected_html)

