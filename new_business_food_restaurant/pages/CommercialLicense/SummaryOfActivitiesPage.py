from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SummaryOfActivitiesPage(BasePage):
    page_name = "Summary Of Activities Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_of_activities_locator")
    btn_legal_form = Button(locator_reader, "btn_legal_form")
    lnk_reselect_the_activities = Link(locator_reader, "lnk_reselect_the_activities")

    def __init__(self):
        super(SummaryOfActivitiesPage, self).__init__(self.page_element)

    def click_legal_form_btn(self):
        self.btn_legal_form.wait_until_location_stable()
        self.btn_legal_form.click()

    def click_reselect_the_activities_link(self):
        self.lnk_reselect_the_activities.wait_until_location_stable()
        self.lnk_reselect_the_activities.click()

