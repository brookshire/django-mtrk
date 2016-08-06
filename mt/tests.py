#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.test import TestCase

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

# from .models import MonitorSite
# from .views import home_page
#
# test_delta = 5
#
#
# class MonitorTests(TestCase):
#     def setUp(self):
#         self.sites = []
#         self.sites.append(MonitorSite.objects.create(name="TestBlah",
#                                                      url="http://www.google.com"))
#         self.sites.append(MonitorSite.objects.create(name="TestSiteTooSmall",
#                                                      url="http://localhost/",
#                                                      display_time=MonitorSite.MIN_DISPLAY_TIME - test_delta))
#         self.sites.append(MonitorSite.objects.create(name="TestSiteTooBig",
#                                                      url="http://localhost/",
#                                                      display_time=MonitorSite.MAX_DISPLAY_TIME + test_delta))
#
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)
#
#     def test_site_display_time_limits(self):
#         # Test default time
#         self.assertEqual(MonitorSite.DEFAULT_DISPLAY_TIME,
#                          self.sites[0].display_time)
#
#         # Test time smaller than minimum
#         self.assertNotEqual(MonitorSite.MIN_DISPLAY_TIME - test_delta,
#                             self.sites[1].display_time)
#         self.assertEqual(MonitorSite.DEFAULT_DISPLAY_TIME, self.sites[1].display_time)
#
#         # Test time larger than maximum
#         self.assertNotEqual(MonitorSite.MAX_DISPLAY_TIME + test_delta,
#                             self.sites[2].display_time)
#         self.assertEqual(MonitorSite.DEFAULT_DISPLAY_TIME, self.sites[2].display_time)
#
#     def test_site_home_content(self):
#         request = HttpRequest()
#         response = home_page(request)
#         expected_html = render_to_string('home.html')
#         # self.assertEqual(response.content.decode(),
#         #                  expected_html)
#
