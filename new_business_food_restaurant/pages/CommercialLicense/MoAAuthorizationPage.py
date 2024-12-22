from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.pages.BasePage import BasePage
import time


class MOAAuthorizationPage(BasePage):
    page_name = "MOA Authorization Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "moa_authorization_locator")
    btn_download_moa = Button(locator_reader, "btn_download_moa")
    btn_create_new_moa = Button(locator_reader, "btn_create_new_moa")
    btn_submit = Button(locator_reader, "btn_submit")

    def __init__(self):
        super(MOAAuthorizationPage, self).__init__(self.page_element)

    def click_create_new_moa_btn(self):
        self.btn_create_new_moa.try_wait_for_absent()
        self.btn_create_new_moa.wait_for_is_present()
        self.btn_create_new_moa.click()

    def click_download_moa(self):
        self.btn_download_moa.try_wait_for_absent()
        self.btn_download_moa.try_wait_for_absent()
        self.btn_download_moa.click()

    def click_submit_btn(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()


