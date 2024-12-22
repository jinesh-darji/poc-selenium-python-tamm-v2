from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ManageApplicationPage(BasePage):
    page_name = "Manage Application Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "manage_application_locator")
    lbl_active = Label(locator_reader, "lbl_active")
    lbl_no_application = Label(locator_reader, "lbl_no_application")

    def __init__(self):
        super(ManageApplicationPage, self).__init__(self.page_element)

    def is_active_text_present(self):
        self.lbl_active.wait_until_location_stable()
        return self.lbl_active.is_displayed() and self.lbl_active.is_present()

    def is_no_restaurant_present(self):
        self.lbl_no_application.wait_until_location_stable()
        return self.lbl_no_application.is_displayed() and self.lbl_no_application.is_present()

