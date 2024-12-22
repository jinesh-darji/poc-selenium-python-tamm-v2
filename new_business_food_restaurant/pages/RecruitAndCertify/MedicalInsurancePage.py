from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MedicalInsurancePage(BasePage):
    page_name = "Medical Insurance Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "medical_insurance_locator")
    lbl_medical_insurance_text = Label(locator_reader, "lbl_medical_insurance_text")

    def __init__(self):
        super(MedicalInsurancePage, self).__init__(self.page_element)

    def is_medical_insurance_text_is_present(self):
        self.lbl_medical_insurance_text.wait_until_location_stable()
        return self.lbl_medical_insurance_text.is_present() and self.lbl_medical_insurance_text.is_displayed()
