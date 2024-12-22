from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AreaDetailsForm(BasePage):
    page_name = "Area Details Form"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "area_detail_locator")
    btn_business_tab = Button(locator_reader, "btn_business_tab")
    btn_population_tab = Button(locator_reader, "btn_population_tab")
    btn_trends_tab = Button(locator_reader, "btn_trends_tab")
    btn_next = Button(locator_reader, "btn_next")

    def __init__(self):
        super(AreaDetailsForm, self).__init__(self.page_element)

    def click_business_tab_btn(self):
        self.btn_business_tab.wait_until_location_stable()
        self.btn_business_tab.click()

    def click_population_tab_btn(self):
        self.btn_population_tab.click()

    def click_trends_tab(self):
        self.btn_trends_tab.click()

    def click_next_btn(self):
        self.btn_next.click()
