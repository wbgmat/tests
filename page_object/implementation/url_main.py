from page_object.interface.url_interface import UrlInterface
from page_object.schema.url_schema import UrlSchema


class UrlMain(UrlInterface,UrlSchema):

    def __init__(self, driver):
        super(UrlMain, self).__init__(driver)

    def get_url(self):
        self.driver.get(self._url)
