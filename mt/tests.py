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
        """
        Create a few sample assets to use for testing below.
        """
        self.assets = []
        self.assets.append(MovieAsset.objects.create(title="FooBar Baz in America",
                                                     barcode="123456789012"))

    def test_default_instance_creation(self):
        """
        Do some sanity testing on the default state of a movie asset
        when it is created.
        """
        for a in self.assets:
            self.assertIsNotNone(a.title)
            self.assertIsNotNone(str(a))
            self.assertIsNotNone(a.added)
            self.assertIsNotNone(a.last_modified)

            default_status_id, default_status_str = AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.UNKNOWN]
            self.assertEqual(default_status_id, a.status)
            self.assertEqual(default_status_str, a.status_str)

    def test_default_asset_transaction(self):
        idx, default_trans_str = AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_IN]

        for a in self.assets:
            tr = AssetTransaction.objects.create(asset=a, trans=AssetTransaction.CHECK_IN)
            # print("%s is %s" % (a, a.status))
            self.assertEqual(AssetTransaction.CHECK_IN, a.status)
            self.assertEqual(default_trans_str, a.status_str)

    def test_all_asset_transactions(self):
        for a in self.assets:

            # Check In
            tr = a.check_in()
            self.assertEqual(a.status, AssetTransaction.CHECK_IN)
            self.assertEqual(a.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_IN][1])
            self.assertEqual(tr.trans, AssetTransaction.CHECK_IN)
            self.assertEqual(tr.asset.status, AssetTransaction.CHECK_IN)
            self.assertEqual(tr.asset.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_IN][1])

            # Check Out
            tr = a.check_out()
            self.assertEqual(a.status, AssetTransaction.CHECK_OUT)
            self.assertEqual(a.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_OUT][1])
            self.assertEqual(tr.trans, AssetTransaction.CHECK_OUT)
            self.assertEqual(tr.asset.status, AssetTransaction.CHECK_OUT)
            self.assertEqual(tr.asset.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.CHECK_OUT][1])

            # Loan
            tr = a.loan("Tester")
            self.assertEqual(a.status, AssetTransaction.LOAN)
            self.assertEqual(tr.note, "Tester")
            self.assertEqual(a.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.LOAN][1])
            self.assertEqual(tr.trans, AssetTransaction.LOAN)
            self.assertEqual(tr.asset.status, AssetTransaction.LOAN)
            self.assertEqual(tr.asset.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.LOAN][1])

            # Unknown
            tr = a.unknown()
            self.assertEqual(a.status, AssetTransaction.UNKNOWN)
            self.assertEqual(a.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.UNKNOWN][1])
            self.assertEqual(tr.trans, AssetTransaction.UNKNOWN)
            self.assertEqual(tr.asset.status, AssetTransaction.UNKNOWN)
            self.assertEqual(tr.asset.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.UNKNOWN][1])

            # Remove
            tr = a.remove()
            self.assertEqual(a.status, AssetTransaction.REMOVED)
            self.assertEqual(a.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.REMOVED][1])
            self.assertEqual(tr.trans, AssetTransaction.REMOVED)
            self.assertEqual(tr.asset.status, AssetTransaction.REMOVED)
            self.assertEqual(tr.asset.status_str,
                             AssetTransaction.TRANSACTION_CHOICES[AssetTransaction.REMOVED][1])

    def test_site_home_content(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # self.assertEqual(response.content.decode(),
        #                  expected_html)

