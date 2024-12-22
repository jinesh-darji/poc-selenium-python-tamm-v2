from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.browser.Browser import Browser
from framework.pages.BasePage import BasePage
from framework.utils.DataReader import DataReader
from framework.utils.LocatorReader import LocatorReader


class MapPage(BasePage):
    page_name = "Map Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "map_locator")
    lbl_map = Label(locator_reader, "lbl_map")

    def __init__(self):
        super(MapPage, self).__init__(self.page_element)

    def is_map_instruction_is_displayed(self):
        self.lbl_map.wait_until_location_stable()
        return self.lbl_map.is_displayed() and self.lbl_map.is_present()

    def lnk_for_show_area_detail(self):
        Browser.set_url(DataReader.get_data("lnk_area.location"))










