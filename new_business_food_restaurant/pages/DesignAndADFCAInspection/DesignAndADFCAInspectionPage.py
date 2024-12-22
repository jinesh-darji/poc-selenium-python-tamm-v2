from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DesignAndADFCAInspectionPage(BasePage):
    page_name = "Design And ADFCA Inspection Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "design_and_adfca_inspection_locator")
    btn_design_and_fitouts = Button(locator_reader, "btn_design_and_fitouts")
    btn_adfca_inspection = Button(locator_reader, "btn_adfca_inspection")
    btn_manage = Button(locator_reader, "btn_manage")

    def __init__(self):
        super(DesignAndADFCAInspectionPage, self).__init__(self.page_element)

    def click_design_and_fitouts_btn(self):
        self.btn_design_and_fitouts.try_wait_for_absent()
        self.btn_design_and_fitouts.wait_for_is_present()
        self.btn_design_and_fitouts.click()

    def click_adfca_inspection_btn(self):
        self.btn_adfca_inspection.try_wait_for_absent()
        self.btn_adfca_inspection.wait_for_is_present()
        self.btn_adfca_inspection.click()

    def click_manage_btn(self):
        self.btn_manage.try_wait_for_absent()
        self.btn_manage.wait_for_is_present()
        self.btn_manage.click()


