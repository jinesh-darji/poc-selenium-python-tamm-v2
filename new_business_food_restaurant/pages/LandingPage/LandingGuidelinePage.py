from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class LandingGuidePage(BasePage):
    page_name = "Landing Guide Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "landing_guide_locator")
    btn_start = Button(locator_reader, "btn_start")

    def __init__(self):
        super(LandingGuidePage, self).__init__(self.page_element)

    def click_start_btn(self):
        self.btn_start.wait_until_location_stable()
        self.btn_start.click()
