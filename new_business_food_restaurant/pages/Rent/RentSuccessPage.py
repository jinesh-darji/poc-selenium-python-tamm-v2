from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RentSuccessPage(BasePage):
    page_name = "Rent Success Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "rent_success_locator")
    btn_schedule_adfca_inspection = Button(locator_reader, "btn_schedule_adfca_inspection")

    def __init__(self):
        super(RentSuccessPage, self).__init__(self.page_element)

    def click_schedule_adfca_inspection_btn(self):
        self.btn_schedule_adfca_inspection.wait_until_location_stable()
        self.btn_schedule_adfca_inspection.click()

