from framework.elements.Button import Button
from framework.elements.TextBox import TextBox
from framework.elements.Dropdown import Dropdown
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class ADFCAPaymentPage(BasePage):
    page_name = "ADFCA Payment Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "adfca_payment_locator")
    txb_card_number = TextBox(locator_reader, "txb_card_number")
    drpdwn_expired_year = Dropdown(locator_reader, "drpdwn_expired_date", "arrow_expired_date")
    btn_payment = Button(locator_reader, "btn_payment")

    def __init__(self):
        super(ADFCAPaymentPage, self).__init__(self.page_element)

    def fill_card_number(self):
        self.txb_card_number.try_wait_for_absent()
        self.txb_card_number.wait_for_is_present()
        for element in self.txb_card_number.get_elements():
            element.send_keys(DataReader.get_data("adfca_payment.card_number"))

    def drpdwn_expired_date(self):
        self.drpdwn_expired_year.try_wait_for_absent()
        self.drpdwn_expired_year.wait_for_is_present()
        self.drpdwn_expired_year.return_and_click_random_data_drpdwn("drpdwn_expired_date", "item_expired_date", "list_expired_date")

    def click_payment_btn(self):
        self.btn_payment.try_wait_for_absent()
        self.btn_payment.wait_for_is_present()
        self.btn_payment.click()



