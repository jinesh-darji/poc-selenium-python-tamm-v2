from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class HowToObtainASAAPage(BasePage):
    page_name = "How To Obtain A SAA Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "obtain_saa_locator")
    lbl_website = Label(locator_reader, "lbl_website")

    def __init__(self):
        super(HowToObtainASAAPage, self).__init__(self.page_element)

    def is_website_is_display(self):
        self.lbl_website.wait_until_location_stable()
        return self.lbl_website.is_displayed() and self.lbl_website.is_present()
