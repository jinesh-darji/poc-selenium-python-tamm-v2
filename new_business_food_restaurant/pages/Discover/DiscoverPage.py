from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverPage(BasePage):
    page_name = "Discover Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "discover_locator")
    btn_get_started = Button(locator_reader, "btn_get_started")

    def __init__(self):
        super(DiscoverPage, self).__init__(self.page_element)

    def click_get_started_btn(self):
        self.btn_get_started.click()
