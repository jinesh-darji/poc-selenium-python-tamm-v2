from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ConductMedicalTestPage(BasePage):
    page_name = "Conduct Medical Test Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "conduct_medical_test_locator")
    lbl_conduct_medical_test_text = Label(locator_reader, "lbl_conduct_medical_test_text")

    def __init__(self):
        super(ConductMedicalTestPage, self).__init__(self.page_element)

    def is_conduct_medical_test_text_is_present(self):
        self.lbl_conduct_medical_test_text.wait_until_location_stable()
        return self.lbl_conduct_medical_test_text.is_present() and self.lbl_conduct_medical_test_text.is_displayed()
