from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button


class LoginTAMMPage(BasePage):

    page_name = "Login TAMM Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "login_tamm_page_locator")
    btn_login_with_smartpass = Button(locator_reader, "btn_login_with_smartpass")
    btn_non_emirati_user_one = Button(locator_reader, "btn_non_emirati_user_one")
    btn_emirati_user_two = Button(locator_reader, "btn_emirati_user_two")
    btn_emirati_user_three = Button(locator_reader, "btn_emirati_user_three")
    btn_non_emirati_user_four = Button(locator_reader, "btn_non_emirati_user_four")
    btn_non_emirati_user_five = Button(locator_reader, "btn_non_emirati_user_five")

    def __init__(self):
        super(LoginTAMMPage, self).__init__(self.page_element)

    def click_login_with_smartpass_btn(self):
        self.btn_login_with_smartpass.wait_until_location_stable()
        self.btn_login_with_smartpass.click()

    def click_non_emirati_user_one_btn(self):
        self.btn_non_emirati_user_one.wait_until_location_stable()
        self.btn_non_emirati_user_one.click()

    def click_emirati_user_two_btn(self):
        self.btn_emirati_user_two.wait_until_location_stable()
        self.btn_emirati_user_two.click()

    def click_emirati_user_three_btn(self):
        self.btn_emirati_user_three.wait_until_location_stable()
        self.btn_emirati_user_three.click()

    def click_non_emirati_user_four_btn(self):
        self.btn_non_emirati_user_four.wait_until_location_stable()
        self.btn_non_emirati_user_four.click()

    def click_non_emirati_user_five_btn(self):
        self.btn_non_emirati_user_five.wait_until_location_stable()
        self.btn_non_emirati_user_five.click()

