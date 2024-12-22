from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RegistrationStepsPage(BasePage):
    page_name = "Registration steps Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "registration_steps_locator")

    def __init__(self):
        super(RegistrationStepsPage, self).__init__(self.page_element)
