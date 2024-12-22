from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ApplyforQuotaPage(BasePage):
    page_name = "Apply for Quota Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "visa_quota_approval_locator")
    lbl_visa_quota_approval_text = Label(locator_reader, "lbl_visa_quota_approval_text")

    def __init__(self):
        super(ApplyforQuotaPage, self).__init__(self.page_element)

    def is_visa_quota_approval_text_is_present(self):
        self.lbl_visa_quota_approval_text.wait_until_location_stable()
        return self.lbl_visa_quota_approval_text.is_present() and self.lbl_visa_quota_approval_text.is_displayed()
