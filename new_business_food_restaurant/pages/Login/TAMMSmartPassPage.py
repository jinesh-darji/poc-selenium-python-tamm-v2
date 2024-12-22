from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.DataReader import DataReader
from framework.utils.LocatorReader import LocatorReader


class TAMMSmartPassPage(BasePage):

    page_name = "TAMM Smart Pass Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "tamm_smart_pass_page_locator")
    txb_username = TextBox(locator_reader, "txb_username")
    txb_password = TextBox(locator_reader, "txb_password")
    btn_login = Button(locator_reader, "btn_login")

    def __init__(self):
        super(TAMMSmartPassPage, self).__init__(self.page_element)

    def fill_username1(self):
        self.txb_username.wait_until_location_stable()
        for element in self.txb_username.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.username1"))

    def fill_password1(self):
        self.txb_password.wait_until_location_stable()
        for element in self.txb_password.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.password1"))

    def fill_username2(self):
        self.txb_username.wait_until_location_stable()
        for element in self.txb_username.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.username2"))

    def fill_password2(self):
        self.txb_password.wait_until_location_stable()
        for element in self.txb_password.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.password2"))

    def fill_username3(self):
        self.txb_username.wait_until_location_stable()
        for element in self.txb_username.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.username3"))

    def fill_password3(self):
        self.txb_password.wait_until_location_stable()
        for element in self.txb_password.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.password3"))

    def fill_username4(self):
        self.txb_username.wait_until_location_stable()
        for element in self.txb_username.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.username4"))

    def fill_password4(self):
        self.txb_password.wait_until_location_stable()
        for element in self.txb_password.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.password4"))

    def fill_username5(self):
        self.txb_username.wait_until_location_stable()
        for element in self.txb_username.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.username5"))

    def fill_password5(self):
        self.txb_password.wait_until_location_stable()
        for element in self.txb_password.get_elements():
            element.send_keys(DataReader.get_data("login_smart_pass.password5"))

    def click_login_button(self):
        self.btn_login.wait_until_location_stable()
        self.btn_login.click()

