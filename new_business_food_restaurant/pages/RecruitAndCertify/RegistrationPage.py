from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RegistrationPage(BasePage):
    page_name = "Registration Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "registration_locator")
    btn_establishment_card = Button(locator_reader, "btn_establishment_card")
    btn_signature_card = Button(locator_reader, "btn_signature_card")
    btn_visa_quota_approval = Button(locator_reader, "btn_visa_quota_approval")
    btn_mohre_establishment_card = Button(locator_reader, "btn_mohre_establishment_card")

    def __init__(self):
        super(RegistrationPage, self).__init__(self.page_element)

    def click_establishment_card_btn(self):
        self.btn_establishment_card.wait_until_location_stable()
        self.btn_establishment_card.click()

    def click_signature_card_btn(self):
        self.btn_signature_card.wait_until_location_stable()
        self.btn_signature_card.click()

    def click_visa_quota_approval_btn(self):
        self.btn_visa_quota_approval.wait_until_location_stable()
        self.btn_visa_quota_approval.click()

    def click_mohre_establishment_card_btn(self):
        self.btn_mohre_establishment_card.wait_until_location_stable()
        self.btn_mohre_establishment_card.click()



