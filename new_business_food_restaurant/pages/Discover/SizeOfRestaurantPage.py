from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Slider import Slider
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SizeOfRestaurantPage(BasePage):
    page_name = "Size Of Restaurant Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "size_of_restaurant_locator")
    lbl_size_of_restaurant = Label(locator_reader, "lbl_size_of_restaurant")
    btn_size_of_restaurant_slider = Slider(locator_reader, "btn_size_of_restaurant_slider")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(SizeOfRestaurantPage, self).__init__(self.page_element)

    def is_display_size_of_restaurant_lable(self):
        self.lbl_size_of_restaurant.wait_until_location_stable()
        self.lbl_size_of_restaurant.is_present()

    def click_size_of_restaurant_slider_btn(self):
        self.btn_size_of_restaurant_slider.wait_until_location_stable()
        self.btn_size_of_restaurant_slider.click_on_slider(10)

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_btn(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()

