from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CommercialLicenseNeworBranchRestaurantPage(BasePage):
    form_name = "Commercial License New or Branch Restaurant Page"
    locator_reader = LocatorReader(form_name)
    page_element = Label(locator_reader, "commercial_license_new_or_branch_restaurant_locator")

    def __init__(self):
        super(CommercialLicenseNeworBranchRestaurantPage, self).__init__(self.page_element)
