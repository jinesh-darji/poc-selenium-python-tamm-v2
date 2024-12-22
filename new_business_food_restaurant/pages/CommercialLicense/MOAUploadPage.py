import os

from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MOAUploadPage(BasePage):
    page_name = "MOA Upload Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "moa_upload_locator")
    btn_upload_moa = Button(locator_reader, "btn_upload_moa")
    btn_submit = Button(locator_reader, "btn_submit")
    pdf_file_path = "ui-automation-nbfr_ACTUAL/new_business_food_restaurant/configuration/test_data"

    def __init__(self):
        super(MOAUploadPage, self).__init__(self.page_element)

    def upload_file_pdf(self, file):
        for document in self.btn_upload_moa.get_elements():
            document.send_keys(os.path.join(self.pdf_file_path, file))

    def upload_document_pdf(self, name_of_file):
        self.upload_file_pdf(name_of_file)

    def is_submit_btn_is_disabled(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.is_disabled()

    def click_btn_submit(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()

