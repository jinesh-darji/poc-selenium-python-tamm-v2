from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SummaryDocumentPage(BasePage):
    page_name = "Summary Document Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_document_locator")
    btn_issue_commercial_license = Button(locator_reader, "btn_issue_commercial_license")
    lnk_reselect_document = Link(locator_reader, "reselect_document")

    def __init__(self):
        super(SummaryDocumentPage, self).__init__(self.page_element)

    def click_issue_commercial_license(self):
        self.btn_issue_commercial_license.try_wait_for_absent()
        self.btn_issue_commercial_license.wait_for_is_present()
        self.btn_issue_commercial_license.click()

    def click_reselect_document(self):
        self.lnk_reselect_document.wait_until_location_stable()
        self.lnk_reselect_document.click()

