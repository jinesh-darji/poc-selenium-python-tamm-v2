from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class WorkPermitPage(BasePage):
    page_name = "Work Permit Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "work_permit_locator")
    lbl_work_permit_text = Label(locator_reader, "lbl_work_permit_text")

    def __init__(self):
        super(WorkPermitPage, self).__init__(self.page_element)

    def is_work_permit_text_is_present(self):
        self.lbl_work_permit_text.wait_until_location_stable()
        return self.lbl_work_permit_text.is_present() and self.lbl_work_permit_text.is_displayed()
