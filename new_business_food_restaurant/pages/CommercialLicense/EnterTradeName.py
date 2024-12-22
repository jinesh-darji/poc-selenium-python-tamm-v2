from framework.elements.Button import Button
from framework.elements.TextBox import TextBox
from framework.elements.Label import Label
from framework.elements.InputDropdown import InputDropdown
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class EnterTradeNamePage(BasePage):
    page_name = "Enter Trade Name Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "enter_trade_name_locator")
    txb_trade_name_english = TextBox(locator_reader, "txb_trade_name_english")
    txb_trade_name_arabic = TextBox(locator_reader, "txb_trade_name_arabic")
    drpdwn_reservation_period = InputDropdown(locator_reader, "drpdwn_reservation_period", "arrow_reservation_period",
                                           "txb_reservation_period")
    btn_submit_for_approval = Button(locator_reader, "btn_submit_for_approval")

    def __init__(self):
        super(EnterTradeNamePage, self).__init__(self.page_element)

    def fill_trade_name_english(self):
        for element in self.txb_trade_name_english.get_elements():
            element.send_keys(DataReader.get_data("enter_trade_name.txb_trade_name_english"))

    def fill_trade_name_arabic(self):
        for element in self.txb_trade_name_arabic.get_elements():
            element.send_keys(DataReader.get_data("enter_trade_name.txb_trade_name_arabic"))

    def select_reservation_months(self, months):
        self.drpdwn_reservation_period.open_dropdown()
        self.drpdwn_reservation_period.select_value(months)

    def click_submit_for_approval_btn(self):
        self.btn_submit_for_approval.try_wait_for_absent()
        self.btn_submit_for_approval.wait_for_is_present()
        self.btn_submit_for_approval.click()

