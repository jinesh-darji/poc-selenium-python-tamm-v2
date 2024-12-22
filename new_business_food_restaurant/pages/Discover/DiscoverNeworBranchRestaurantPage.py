from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class DiscoverNeworBranchRestaurantPage(BasePage):
    form_name = "Discover New or Branch Restaurant Page"
    locator_reader = LocatorReader(form_name)
    page_element = Label(locator_reader, "discover_new_or_branch_restaurant_locator")
    btn_new_company = Button(locator_reader, "btn_new_company")
    btn_uae_branch = Button(locator_reader, "btn_uae_branch")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")

    def __init__(self):
        super(DiscoverNeworBranchRestaurantPage, self).__init__(self.page_element)

    def click_new_restaurant_btn(self):
        self.btn_new_company.wait_until_location_stable()
        self.btn_new_company.click()

    def click_uae_branch_btn(self):
        self.btn_uae_branch.wait_until_location_stable()
        self.btn_uae_branch.click()

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_btn(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()
