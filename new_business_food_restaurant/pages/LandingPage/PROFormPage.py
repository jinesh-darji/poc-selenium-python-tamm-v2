from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.DataReader import DataReader
from framework.utils.LocatorReader import LocatorReader


class PROFormPage(BasePage):
    page_name = "PRO Form Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "assign_pro_form_locator")
    txb_name_english = TextBox(locator_reader, "txb_name_english")
    txb_name_arabic = TextBox(locator_reader, "txb_name_arabic")
    txb_emirati_id = TextBox(locator_reader, "txb_emirati_id")
    txb_email = TextBox(locator_reader, "txb_email")
    txb_phone_number = TextBox(locator_reader, "txb_phone_number")
    btn_assign_pro = Button(locator_reader, "btn_assign_pro")
    btn_cancel_request = Button(locator_reader, "btn_cancel_request")

    def __init__(self):
        super(PROFormPage, self).__init__(self.page_element)

    def fill_name_english(self):
        for element in self.txb_name_english.get_elements():
            element.send_keys(DataReader.get_data("assign_pro.name_english"))

    def fill_name_arabic(self):
        for element in self.txb_name_arabic.get_elements():
            element.send_keys(DataReader.get_data("assign_pro.name_arabic"))

    def fill_emirati_id(self):
        for element in self.txb_emirati_id.get_elements():
            element.send_keys(DataReader.get_data("assign_pro.emirati_id"))

    def fill_email(self):
        for element in self.txb_email.get_elements():
            element.send_keys(DataReader.get_data("assign_pro.email"))

    def fill_phone_number(self):
        for element in self.txb_phone_number.get_elements():
            element.send_keys(DataReader.get_data("assign_pro.phone_number"))

    def click_assign_pro_btn(self):
        self.btn_assign_pro.click()

    def click_cancel_request_btn(self):
        self.btn_cancel_request.click()



