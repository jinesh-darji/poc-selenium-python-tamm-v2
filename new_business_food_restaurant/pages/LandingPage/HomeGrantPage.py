from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.elements.Label import Label


class HomeGrantPage(BasePage):
    page_name = "Home Grant Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "home_grant_page_locator")
    btn_start_a_new_restaurant = Button(locator_reader, "btn_start_a_new_restaurant")
    btn_manage_application = Button(locator_reader, "btn_manage_application")
    btn_market_reports = Button(locator_reader, "btn_market_reports")
    btn_side_menu = Button(locator_reader, "btn_side_menu")
    btn_header_logo = Button(locator_reader, "btn_header_logo")
    btn_login = Button(locator_reader, "btn_login")

    def __init__(self):
        super(HomeGrantPage, self).__init__(self.page_element)

    def click_start_a_new_restaurant_btn(self):
        self.btn_start_a_new_restaurant.wait_until_location_stable()
        self.btn_start_a_new_restaurant.click()

    def click_manage_application_btn(self):
        self.btn_manage_application.wait_until_location_stable()
        self.btn_manage_application.click()

    def click_market_reports_btn(self):
        self.btn_market_reports.wait_until_location_stable()
        self.btn_market_reports.click()

    def click_side_menu_btn(self):
        self.btn_side_menu.wait_until_location_stable()
        self.btn_side_menu.click()

    def click_header_logo_btn(self):
        self.btn_header_logo.wait_until_location_stable()
        self.btn_header_logo.click()

    def click_login_btn(self):
        self.btn_login.wait_until_location_stable()
        self.btn_login.click()

