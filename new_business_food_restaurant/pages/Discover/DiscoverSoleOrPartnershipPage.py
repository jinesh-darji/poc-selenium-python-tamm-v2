from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverSoleOrPartnershipPage(BasePage):
    page_name = "Discover Sole Or Partnership Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "discover_sole_or_partnership_locator")
    btn_sole = Button(locator_reader, "btn_sole")
    btn_partnership = Button(locator_reader, "btn_partnership")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(DiscoverSoleOrPartnershipPage, self).__init__(self.page_element)

    def click_sole_btn(self):
        self.btn_sole.wait_until_location_stable()
        self.btn_sole.click()

    def click_partnership_btn(self):
        self.btn_partnership.wait_until_location_stable()
        self.btn_partnership.click()

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_btn(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()
