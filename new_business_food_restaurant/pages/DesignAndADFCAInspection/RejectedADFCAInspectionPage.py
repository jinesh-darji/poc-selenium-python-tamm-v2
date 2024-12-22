from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RejectedADFCAInspectionPage(BasePage):
    page_name = "Rejected ADFCA Inspection Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "rejected_adfca_inspection_locator")
    btn_submit_request = Button(locator_reader, "btn_submit_request")
    lnk_design_and_adfca_inspection = Link(locator_reader, "lnk_design_and_adfca_inspection")
    lbl_reject_description = Label(locator_reader, "lbl_reject_description")

    def __init__(self):
        super(RejectedADFCAInspectionPage, self).__init__(self.page_element)

    def click_submit_request_btn(self):
        self.btn_submit_request.wait_until_location_stable()
        self.btn_submit_request.click()

    def click_design_and_adfca_inspection_link(self):
        self.lnk_design_and_adfca_inspection.click()

    def is_lbl_reject_description_is_present(self):
        self.lbl_reject_description.try_wait_for_absent()
        self.lbl_reject_description.wait_for_is_present()
        return self.lbl_reject_description.is_displayed() and self.lbl_reject_description.is_present()
