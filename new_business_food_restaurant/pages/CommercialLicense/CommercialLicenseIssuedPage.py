from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CommercialLicenseIssuedPage(BasePage):
    page_name = "Commercial License Issued Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "commercial_license_issued_locator")
    btn_download_certificate = Button(locator_reader, "btn_download_certificate")
    btn_schedule_adfca_inspection = Button(locator_reader, "btn_schedule_adfca_inspection")
    btn_rent = Button(locator_reader, "btn_rent")

    def __init__(self):
        super(CommercialLicenseIssuedPage, self).__init__(self.page_element)

    def click_download_certificate_btn(self):
        self.btn_download_certificate.wait_for_is_present()
        self.btn_download_certificate.click()

    def click_schedule_adfca_inspection_btn(self):
        self.btn_schedule_adfca_inspection.wait_for_is_present()
        self.btn_schedule_adfca_inspection.click()

    def click_rent_btn(self):
        self.btn_rent.try_wait_for_absent()
        self.btn_rent.wait_for_is_present()
        self.btn_rent.click()

