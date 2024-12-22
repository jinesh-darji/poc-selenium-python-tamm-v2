from framework.elements.Button import Button
from framework.elements.Checkbox import Checkbox
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CommercialLicenseServiceListPage(BasePage):
    page_name = "Commercial License Service List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "commercial_license_service_list_locator")
    chbx_bakery = Checkbox(locator_reader, "btn_bakery")
    chbx_fast_food = Checkbox(locator_reader, "btn_fast_food")
    chbx_fresh_juices = Checkbox(locator_reader, "btn_fresh_juices")
    chbx_grills = Checkbox(locator_reader, "btn_grills")
    chbx_hot_cold_beverages = Checkbox(locator_reader, "btn_hot_cold_beverages")
    chbx_light_meal = Checkbox(locator_reader, "btn_light_meal")
    chbx_pastries = Checkbox(locator_reader, "btn_pastries")
    chbx_salads_appetizers = Checkbox(locator_reader, "btn_salads_appetizers")
    chbx_seafood = Checkbox(locator_reader, "btn_seafood")
    chbx_sweets = Checkbox(locator_reader, "btn_sweets")
    chbx_event_catering = Checkbox(locator_reader, "btn_event_catering")
    chbx_bakery_checked = Checkbox(locator_reader, "btn_bakery_checked")
    chbx_fast_food_checked = Checkbox(locator_reader, "btn_fast_food_checked")
    chbx_fresh_juices_checked = Checkbox(locator_reader, "btn_fresh_juices_checked")
    chbx_grills_checked = Checkbox(locator_reader, "btn_grills_checked")
    chbx_hot_cold_beverages_checked = Checkbox(locator_reader, "btn_hot_cold_beverages_checked")
    chbx_light_meal_checked = Checkbox(locator_reader, "btn_light_meal_checked")
    chbx_pastries_checked = Checkbox(locator_reader, "btn_pastries_checked")
    chbx_salads_appetizers_checked = Checkbox(locator_reader, "btn_salads_appetizers_checked")
    chbx_seafood_checked = Checkbox(locator_reader, "btn_seafood_checked")
    chbx_sweets_checked = Checkbox(locator_reader, "btn_sweets_checked")
    chbx_event_catering_checked = Checkbox(locator_reader, "btn_event_catering_checked")
    btn_next = Button(locator_reader, "btn_next")

    def __init__(self):
        super(CommercialLicenseServiceListPage, self).__init__(self.page_element)

    def click_bakery_btn(self):
        self.chbx_bakery.wait_until_location_stable()
        self.chbx_bakery.click()

    def click_fast_food_btn(self):
        self.chbx_fast_food.click()

    def click_fresh_juices_btn(self):
        self.chbx_fresh_juices.click()

    def click_grills_btn(self):
        self.chbx_grills.click()

    def click_hot_cold_behaviour_btn(self):
        self.chbx_hot_cold_beverages.click()

    def click_light_meal_btn(self):
        self.chbx_light_meal.click()

    def click_pastries_btn(self):
        self.chbx_pastries.click()

    def click_salad_appetizers_btn(self):
        self.chbx_salads_appetizers.click()

    def click_seafood_btn(self):
        self.chbx_seafood.click()

    def click_sweets_btn(self):
        self.chbx_sweets.click()

    def click_event_catering_btn(self):
        self.chbx_event_catering.click()

    def click_next_btn(self):
        self.btn_next.click()
