from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.InputDropdown import InputDropdown
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
import time


class HomePage(BasePage):

    page_name = "Home Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "home_page_locator")
    btn_discover_start = Button(locator_reader, "btn_discover_start")
    btn_commercial_license_start = Button(locator_reader, "btn_commercial_license_start")
    btn_financing_start = Button(locator_reader, "btn_financing_start")
    btn_rent_start = Button(locator_reader, "btn_rent_start")
    btn_design_and_adfca_inspection_start = Button(locator_reader, "btn_design_and_adfca_inspection_start")
    btn_recruit_and_certify_start = Button(locator_reader, "btn_recruit_and_certify_start")
    btn_pro = Button(locator_reader, "btn_pro")
    btn_side_menu_discover = Button(locator_reader, "btn_side_menu_discover")
    btn_side_menu_commercial_license = Button(locator_reader, "btn_side_menu_commercial_license")
    btn_side_menu_financing = Button(locator_reader, "btn_side_menu_financing")
    btn_side_menu_rent = Button(locator_reader, "btn_side_menu_rent")
    btn_side_menu_design_and_adfca_inspection = Button(locator_reader, "btn_side_menu_design_and_adfca_inspection")
    btn_side_menu_recruit_and_certify = Button(locator_reader, "btn_side_menu_recruit_and_certify")
    drpdwn_my_application = InputDropdown(locator_reader, "my_application_drop_down", "my_application_arrow", "txb_my_application")
    btn_financing_tab = Button(locator_reader, "btn_financing_tab")

    def __init__(self):
        super(HomePage, self).__init__(self.page_element)

    def click_pro_btn(self):
        self.btn_pro.try_wait_for_absent()
        self.btn_pro.wait_for_is_present()
        self.btn_pro.click()

    def click_discover_start_btn(self):
        self.btn_discover_start.wait_until_location_stable()
        self.btn_discover_start.click()

    def click_commercial_license_start_btn(self):
        self.btn_commercial_license_start.wait_until_location_stable()
        self.btn_commercial_license_start.click()

    def click_financing_start_btn(self):
        self.btn_financing_start.try_wait_for_absent()
        self.btn_financing_start.wait_for_is_present()
        self.btn_financing_start.click()

    def click_rent_start_btn(self):
        self.btn_rent_start.try_wait_for_absent()
        self.btn_rent_start.wait_for_is_present()
        self.btn_rent_start.click()

    def click_design_and_adfca_inspection_start_btn(self):
        self.btn_design_and_adfca_inspection_start.try_wait_for_absent()
        self.btn_design_and_adfca_inspection_start.wait_for_is_present()
        self.btn_design_and_adfca_inspection_start.click()

    def click_recruit_and_certify_start_btn(self):
        self.btn_recruit_and_certify_start.try_wait_for_absent()
        self.btn_recruit_and_certify_start.wait_for_is_present()
        self.btn_recruit_and_certify_start.click()

    def select_application(self, application):
        self.drpdwn_my_application.wait_until_location_stable()
        self.drpdwn_my_application.open_dropdown()
        self.drpdwn_my_application.select_value(application)
        time.sleep(2)

    def select_financing_tab(self):
        self.btn_financing_tab.try_wait_for_absent()
        self.btn_financing_tab.wait_for_is_present()
        self.btn_financing_tab.click()

