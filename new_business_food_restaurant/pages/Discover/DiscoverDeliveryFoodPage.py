from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverDeliveryFoodPage(BasePage):
    page_name = "Discover Delivery Food Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "discover_delivery_food_locator")
    btn_yes = Button(locator_reader, "btn_yes")
    btn_no = Button(locator_reader, "btn_no")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(DiscoverDeliveryFoodPage, self).__init__(self.page_element)

    def click_yes_btn(self):
        self.btn_yes.wait_until_location_stable()
        self.btn_yes.click()

    def click_no_btn(self):
        self.btn_no.wait_until_location_stable()
        self.btn_no.click()

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_button(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()
