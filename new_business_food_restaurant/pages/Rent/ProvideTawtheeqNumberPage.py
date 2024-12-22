from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class ProvideTawtheeqNumberPage(BasePage):
    page_name = "Provide Tawtheeq Number Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "provide_tawtheeq_number_locator")
    txb_tawtheeq_number = TextBox(locator_reader, "txb_tawtheeq_number")
    btn_submit = Button(locator_reader, "btn_submit")
    btn_payment = Button(locator_reader, "btn_payment")
    lbl_registration_fee = Label(locator_reader, "lbl_registration_fee")

    def __init__(self):
        super(ProvideTawtheeqNumberPage, self).__init__(self.page_element)

    def fill_tawtheeq_number(self):
        for element in self.txb_tawtheeq_number.get_elements():
            element.send_keys(DataReader.get_data("provide_tawtheeq_number.tawtheeq_number"))

    def click_submit_btn(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()

    def click_payment_btn(self):
        self.btn_payment.try_wait_for_absent()
        self.btn_payment.wait_for_is_present()
        self.btn_payment.click()

    def is_registration_fee_is_present(self):
        self.lbl_registration_fee.try_wait_for_absent()
        self.lbl_registration_fee.wait_for_is_present()
        return self.lbl_registration_fee.is_present() and self.lbl_registration_fee.is_displayed()
