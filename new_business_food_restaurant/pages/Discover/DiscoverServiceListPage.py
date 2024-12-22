from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverServiceListPage(BasePage):

    page_name = "Discover Service List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "discover_service_list_locator")
    btn_bakery = Button(locator_reader, "btn_bakery")
    btn_fast_food = Button(locator_reader, "btn_fast_food")
    btn_fresh_juices = Button(locator_reader, "btn_fresh_juices")
    btn_grills = Button(locator_reader, "btn_grills")
    btn_hot_cold_beverages = Button(locator_reader, "btn_hot_cold_beverages")
    btn_light_meal = Button(locator_reader, "btn_light_meal")
    btn_pastries = Button(locator_reader, "btn_pastries")
    btn_salads_appetizers = Button(locator_reader, "btn_salads_appetizers")
    btn_seafood = Button(locator_reader, "btn_seafood")
    btn_sweets = Button(locator_reader, "btn_sweets")
    btn_event_catering = Button(locator_reader, "btn_event_catering")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(DiscoverServiceListPage, self).__init__(self.page_element)

    def click_bakery_btn(self):
        self.btn_bakery.wait_until_location_stable()
        self.btn_bakery.click()

    def click_fast_food_btn(self):
        self.btn_fast_food.wait_until_location_stable()
        self.btn_fast_food.click()

    def click_fresh_juices_btn(self):
        self.btn_fresh_juices.wait_until_location_stable()
        self.btn_fresh_juices.click()

    def click_grills_btn(self):
        self.btn_grills.wait_until_location_stable()
        self.btn_grills.click()

    def click_hot_cold_behaviour_btn(self):
        self.btn_hot_cold_beverages.wait_until_location_stable()
        self.btn_hot_cold_beverages.click()

    def click_light_meal_btn(self):
        self.btn_light_meal.wait_until_location_stable()
        self.btn_light_meal.click()

    def click_pastries_btn(self):
        self.btn_pastries.wait_until_location_stable()
        self.btn_pastries.click()

    def click_salad_appetizers_btn(self):
        self.btn_salads_appetizers.wait_until_location_stable()
        self.btn_salads_appetizers.click()

    def click_seafood_btn(self):
        self.btn_seafood.wait_until_location_stable()
        self.btn_seafood.click()

    def click_sweets_btn(self):
        self.btn_sweets.wait_until_location_stable()
        self.btn_sweets.click()

    def click_event_catering_btn(self):
        self.btn_event_catering.wait_until_location_stable()
        self.btn_event_catering.click()

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_button(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()
