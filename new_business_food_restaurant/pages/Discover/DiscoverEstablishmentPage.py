from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverEstablishmentPage(BasePage):
    page_name = "Discover Establishment Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "discover_establishment_locator")
    btn_llc = Button(locator_reader, "btn_llc")
    btn_establishment = Button(locator_reader, "btn_establishment")
    btn_sole_proprietorship_llc = Button(locator_reader, "btn_sole_proprietorship_llc")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(DiscoverEstablishmentPage, self).__init__(self.page_element)

    def click_llc_btn(self):
        self.btn_llc.wait_until_location_stable()
        self.btn_llc.click()

    def click_establishment_btn(self):
        self.btn_establishment.wait_until_location_stable()
        self.btn_establishment.click()

    def click_sole_proprietorship_llc_btn(self):
        self.btn_sole_proprietorship_llc.wait_until_location_stable()
        self.btn_sole_proprietorship_llc.click()

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_btn(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()
