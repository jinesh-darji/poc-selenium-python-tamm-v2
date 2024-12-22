from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MOAPage(BasePage):
    page_name = "MOA Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "moa_locator")
    btn_emoa = Button(locator_reader, "btn_emoa")
    btn_upload = Button(locator_reader, "btn_upload")
    btn_reference_number = Button(locator_reader, "btn_reference_number")

    def __init__(self):
        super(MOAPage, self).__init__(self.page_element)

    def click_emoa_btn(self):
        self.btn_emoa.wait_until_location_stable()
        self.btn_emoa.click()

    def click_upload_btn(self):
        self.btn_upload.wait_until_location_stable()
        self.btn_upload.click()

    def click_reference_number_btn(self):
        self.btn_reference_number.wait_until_location_stable()
        self.btn_reference_number.click()





