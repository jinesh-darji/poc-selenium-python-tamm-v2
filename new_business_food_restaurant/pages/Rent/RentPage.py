from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RentPage(BasePage):
    page_name = "Rent Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "rent_locator")
    btn_find_place = Button(locator_reader, "btn_find_place")
    btn_provide_tawtheeq_number = Button(locator_reader, "btn_provide_tawtheeq_number")

    def __init__(self):
        super(RentPage, self).__init__(self.page_element)

    def click_find_place_btn(self):
        self.btn_find_place.wait_until_location_stable()
        self.btn_find_place.click()

    def click_provide_tawtheeq_number_btn(self):
        self.btn_provide_tawtheeq_number.wait_until_location_stable()
        self.btn_provide_tawtheeq_number.click()



