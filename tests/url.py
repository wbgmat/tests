import unittest
from page_object.interface.url_interface import UrlInterface
from page_object.interface.base_test_case import BaseTestCase
from page_object.schema.url_schema import UrlSchema
from page_object.implementation.url_main import UrlMain


class Url(BaseTestCase):

    def test_url(self):
        obi = UrlMain(self.driver)
        obi.get_url()
        obi.__mro__

if __name__ == "__main__":
    unittest.main(verbosity=2)