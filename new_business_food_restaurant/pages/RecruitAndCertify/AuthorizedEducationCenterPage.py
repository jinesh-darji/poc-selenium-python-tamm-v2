from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AuthorizedEducationCenterPage(BasePage):
    page_name = "Authorized Education Center Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "authorized_education_center_locator")
    lbl_center_name = Label(locator_reader, "lbl_center_name")

    def __init__(self):
        super(AuthorizedEducationCenterPage, self).__init__(self.page_element)

    def is_center_name_present(self):
        self.lbl_center_name.wait_until_location_stable()
        return self.lbl_center_name.is_present() and self.lbl_center_name.is_displayed()

