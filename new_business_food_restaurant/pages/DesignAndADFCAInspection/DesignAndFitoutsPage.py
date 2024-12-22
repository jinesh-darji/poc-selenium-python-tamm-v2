from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DesignAndFitoutsPage(BasePage):
    page_name = "Design And Fitouts Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "design_and_fitouts_locator")
    btn_search_consultants = Button(locator_reader, "btn_search_consultants")
    btn_search_contractors = Button(locator_reader, "btn_search_contractors")
    lnk_design_and_adfca_inspection = Link(locator_reader, "lnk_design_and_adfca_inspection")

    def __init__(self):
        super(DesignAndFitoutsPage, self).__init__(self.page_element)

    def click_search_consultants_btn(self):
        self.btn_search_consultants.try_wait_for_absent()
        self.btn_search_consultants.wait_for_is_present()
        self.btn_search_consultants.click()

    def click_search_contractors_btn(self):
        self.btn_search_contractors.try_wait_for_absent()
        self.btn_search_contractors.wait_for_is_present()
        self.btn_search_contractors.click()

    def click_design_and_adfca_inspection_link(self):
        self.lnk_design_and_adfca_inspection.try_wait_for_absent()
        self.lnk_design_and_adfca_inspection.wait_for_is_present()
        self.lnk_design_and_adfca_inspection.click()

