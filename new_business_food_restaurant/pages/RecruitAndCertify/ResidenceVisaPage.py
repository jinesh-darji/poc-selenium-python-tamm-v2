from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ResidenceVisaPage(BasePage):
    page_name = "Residence Visa Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "residence_visa_locator")
    lbl_residence_visa_text = Label(locator_reader, "lbl_residence_visa_text")

    def __init__(self):
        super(ResidenceVisaPage, self).__init__(self.page_element)

    def is_residence_visa_text_is_present(self):
        self.lbl_residence_visa_text.wait_until_location_stable()
        return self.lbl_residence_visa_text.is_present() and self.lbl_residence_visa_text.is_displayed()
