from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class WorkOfferPage(BasePage):
    page_name = "Work Offer Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "work_offer_locator")
    lbl_work_offer_text = Label(locator_reader, "lbl_work_offer_text")
    lnk_work_offer_side_menu = Link(locator_reader, "lnk_work_offer_side_menu")
    lnk_work_permit_side_menu = Link(locator_reader, "lnk_work_permit_side_menu")
    lnk_entry_permit_side_menu = Link(locator_reader, "lnk_entry_permit_side_menu")
    lnk_medical_test_side_menu = Link(locator_reader, "lnk_medical_test_side_menu")
    lnk_work_contract_side_menu = Link(locator_reader, "lnk_work_contract_side_menu")
    lnk_medical_insurance_side_menu = Link(locator_reader, "lnk_medical_insurance_side_menu")
    lnk_emirates_id_side_menu = Link(locator_reader, "lnk_emirates_id_side_menu")
    lnk_residence_visa_side_menu = Link(locator_reader, "lnk_residence_visa_side_menu")

    def __init__(self):
        super(WorkOfferPage, self).__init__(self.page_element)

    def is_work_offer_text_is_present(self):
        self.lbl_work_offer_text.wait_until_location_stable()
        return self.lbl_work_offer_text.is_present() and self.lbl_work_offer_text.is_displayed()

    def click_work_offer_side_menu_link(self):
        self.lnk_work_offer_side_menu.wait_until_location_stable()
        self.lnk_work_offer_side_menu.click()

    def click_work_permit_side_menu_link(self):
        self.lnk_work_permit_side_menu.wait_until_location_stable()
        self.lnk_work_permit_side_menu.click()

    def click_entry_permit_side_menu_link(self):
        self.lnk_entry_permit_side_menu.wait_until_location_stable()
        self.lnk_entry_permit_side_menu.click()

    def click_medical_test_side_menu_link(self):
        self.lnk_medical_test_side_menu.wait_until_location_stable()
        self.lnk_medical_test_side_menu.click()

    def click_work_contract_side_menu_link(self):
        self.lnk_work_contract_side_menu.wait_until_location_stable()
        self.lnk_work_contract_side_menu.click()

    def click_medical_insurance_side_menu_link(self):
        self.lnk_medical_insurance_side_menu.wait_until_location_stable()
        self.lnk_medical_insurance_side_menu.click()

    def click_emirates_id_side_menu_link(self):
        self.lnk_emirates_id_side_menu.wait_until_location_stable()
        self.lnk_emirates_id_side_menu.click()

    def click_residence_visa_side_menu_link(self):
        self.lnk_residence_visa_side_menu.wait_until_location_stable()
        self.lnk_residence_visa_side_menu.click()
