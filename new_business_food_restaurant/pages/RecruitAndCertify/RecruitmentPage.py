from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RecruitmentPage(BasePage):
    page_name = "Recruitment Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "recruitment_locator")
    btn_work_offer = Button(locator_reader, "btn_work_offer")
    btn_work_permit = Button(locator_reader, "btn_work_permit")
    btn_entry_permit = Button(locator_reader, "btn_entry_permit")
    btn_medical_test = Button(locator_reader, "btn_medical_test")
    btn_work_contract = Button(locator_reader, "btn_work_contract")
    btn_medical_insurance = Button(locator_reader, "btn_medical_insurance")
    btn_emirates_id = Button(locator_reader, "btn_emirates_id")
    btn_residence_visa = Button(locator_reader, "btn_residence_visa")

    def __init__(self):
        super(RecruitmentPage, self).__init__(self.page_element)

    def click_work_offer_btn(self):
        self.btn_work_offer.wait_until_location_stable()
        self.btn_work_offer.click()

    def click_work_permit_btn(self):
        self.btn_work_permit.wait_until_location_stable()
        self.btn_work_permit.click()

    def click_entry_permit_btn(self):
        self.btn_entry_permit.wait_until_location_stable()
        self.btn_entry_permit.click()

    def click_medical_test_btn(self):
        self.btn_medical_test.wait_until_location_stable()
        self.btn_medical_test.click()

    def click_work_contract_btn(self):
        self.btn_work_contract.wait_until_location_stable()
        self.btn_work_contract.click()

    def click_medical_insurance_btn(self):
        self.btn_medical_insurance.wait_until_location_stable()
        self.btn_medical_insurance.click()

    def click_emirates_id_btn(self):
        self.btn_emirates_id.wait_until_location_stable()
        self.btn_emirates_id.click()

    def click_residence_visa_btn(self):
        self.btn_residence_visa.wait_until_location_stable()
        self.btn_residence_visa.click()
