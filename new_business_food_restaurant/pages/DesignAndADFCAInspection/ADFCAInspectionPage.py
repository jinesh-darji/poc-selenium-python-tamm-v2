from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ADFCAInspectionPage(BasePage):
    page_name = "ADFCA Inspection Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "adfca_inspection_locator")
    btn_schedule_adfca_inspection = Button(locator_reader, "btn_schedule_adfca_inspection")
    lnk_design_and_adfca_inspection = Link(locator_reader, "lnk_design_and_adfca_inspection")
    lnk_application = Link(locator_reader, "lnk_application")

    def __init__(self):
        super(ADFCAInspectionPage, self).__init__(self.page_element)

    def click_schedule_adfca_inspection(self):
        self.btn_schedule_adfca_inspection.try_wait_for_absent()
        self.btn_schedule_adfca_inspection.wait_for_is_present()
        self.btn_schedule_adfca_inspection.click()

    def click_design_adfca_inspection_link(self):
        self.lnk_design_and_adfca_inspection.try_wait_for_absent()
        self.lnk_design_and_adfca_inspection.wait_for_is_present()
        self.lnk_design_and_adfca_inspection.click()

    def click_application_link(self):
        self.lnk_application.try_wait_for_absent()
        self.lnk_application.wait_for_is_present()
        self.lnk_application.click()
