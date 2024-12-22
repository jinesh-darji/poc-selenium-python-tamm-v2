from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
import time


class MarketReportPage(BasePage):
    page_name = "Market Report Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "market_report_locator")
    lbl_template_one = Label(locator_reader, "lbl_template_one")
    lbl_template_two = Label(locator_reader, "lbl_template_two")
    lbl_template_three = Label(locator_reader, "lbl_template_three")
    lbl_template_four = Label(locator_reader, "lbl_template_four")
    lbl_template_five = Label(locator_reader, "lbl_template_five")

    def __init__(self):
        super(MarketReportPage, self).__init__(self.page_element)

    def is_template_one_is_displayed(self):
        self.lbl_template_one.wait_until_location_stable()
        return self.lbl_template_one.is_present() and self.lbl_template_one.is_displayed()

    def is_template_two_is_displayed(self):
        self.lbl_template_two.wait_until_location_stable()
        return self.lbl_template_two.is_present() and self.lbl_template_two.is_displayed()

    def is_template_three_is_displayed(self):
        self.lbl_template_three.wait_until_location_stable()
        return self.lbl_template_three.is_present() and self.lbl_template_three.is_displayed()

    def is_template_four_is_displayed(self):
        self.lbl_template_four.wait_until_location_stable()
        return self.lbl_template_four.is_present() and self.lbl_template_four.is_displayed()

    def is_template_five_is_displayed(self):
        self.lbl_template_five.wait_until_location_stable()
        return self.lbl_template_five.is_present() and self.lbl_template_five.is_displayed()

    def click_template_one(self):
        self.lbl_template_one.click()
        time.sleep(3)

    def click_template_two(self):
        self.lbl_template_two.click()
        time.sleep(3)

    def click_template_three(self):
        self.lbl_template_three.click()
        time.sleep(3)

    def click_template_four(self):
        self.lbl_template_four.click()
        time.sleep(3)

    def click_template_five(self):
        self.lbl_template_five.click()
        time.sleep(3)
