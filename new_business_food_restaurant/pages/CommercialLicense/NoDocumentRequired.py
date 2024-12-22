from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button


class NoDocumentRequiredPage(BasePage):
    page_name = "No Document Required Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "no_document_required_locator")
    lbl_no_document_required = Label(locator_reader, "lbl_no_document_required")
    btn_issue_commercial_license = Button(locator_reader, "btn_issue_commercial_license")

    def __init__(self):
        super(NoDocumentRequiredPage, self).__init__(self.page_element)

    def is_no_document_required_display(self):
        return self.lbl_no_document_required.is_present() and self.lbl_no_document_required.is_displayed()

    def click_issue_commercial_license_btn(self):
        self.btn_issue_commercial_license.wait_until_location_stable()
        self.btn_issue_commercial_license.click()

