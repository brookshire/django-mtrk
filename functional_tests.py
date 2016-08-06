#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_visit_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('MTRK', self.browser.title)
        # table = self.browser.find_element_by_id('MonitorSitesTable')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertGreaterEqual(len(rows), 1)


if __name__ == '__main__':
    unittest.main()
