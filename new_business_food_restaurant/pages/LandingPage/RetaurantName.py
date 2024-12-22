from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader
from framework.elements.TextBox import TextBox
from framework.elements.Button import Button


class RestaurantNamePage(BasePage):

    page_name = "Restaurant Name Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "restaurant_name_page_locator")
    txb_restaurant_name = TextBox(locator_reader, "txb_restaurant_name")
    btn_start = Button(locator_reader, "btn_start")

    def __init__(self):
        super(RestaurantNamePage, self).__init__(self.page_element)

    def fill_restaurant_name(self):
        self.txb_restaurant_name.wait_until_location_stable()
        for element in self.txb_restaurant_name.get_elements():
            element.send_keys(DataReader.get_data("restaurant_name.name"))

    def click_start_btn(self):
        self.btn_start.wait_until_location_stable()
        self.btn_start.click()
