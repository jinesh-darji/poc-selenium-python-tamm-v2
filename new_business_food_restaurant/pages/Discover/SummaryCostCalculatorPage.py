from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
import time


class SummaryCostCalculatorPage(BasePage):
    page_name = "Summary Cost Calculator Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_cost_calculator")
    btn_get_commercial_license = Button(locator_reader, "btn_get_commercial_license")
    btn_print = Button(locator_reader, "btn_print")

    def __init__(self):
        super(SummaryCostCalculatorPage, self).__init__(self.page_element)

    def click_commercial_license_btn(self):
        self.btn_get_commercial_license.wait_until_location_stable()
        self.btn_get_commercial_license.click()

    def click_print_btn(self):
        self.btn_print.wait_until_location_stable()
        self.btn_print.click()
        time.sleep(3)
