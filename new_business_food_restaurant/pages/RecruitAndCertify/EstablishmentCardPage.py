from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EstablishmentCardPage(BasePage):
    page_name = "Establishment Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "establishment_card_locator")
    lbl_establishment_card_text = Label(locator_reader, "lbl_establishment_card_text")
    lnk_establishment_card_side_menu = Link(locator_reader, "lnk_establishment_card_side_menu")
    lnk_electronic_signature_card_side_menu = Link(locator_reader, "lnk_electronic_signature_card_side_menu")
    lnk_mohre_establishment_card_side_menu = Link(locator_reader, "lnk_mohre_establishment_card_side_menu")
    lnk_visa_quota_approval_side_menu = Link(locator_reader, "lnk_visa_quota_approval_side_menu")

    def __init__(self):
        super(EstablishmentCardPage, self).__init__(self.page_element)

    def is_establishment_card_text_is_present(self):
        self.lbl_establishment_card_text.wait_until_location_stable()
        return self.lbl_establishment_card_text.is_present() and self.lbl_establishment_card_text.is_displayed()

    def click_establishment_card_link(self):
        self.lnk_establishment_card_side_menu.wait_until_location_stable()
        self.lnk_establishment_card_side_menu.click()

    def click_esignature_card_link(self):
        self.lnk_electronic_signature_card_side_menu.wait_until_location_stable()
        self.lnk_electronic_signature_card_side_menu.click()

    def click_mohre_establishment_card_link(self):
        self.lnk_mohre_establishment_card_side_menu.wait_until_location_stable()
        self.lnk_mohre_establishment_card_side_menu.click()

    def click_visa_quota_approval_link(self):
        self.lnk_visa_quota_approval_side_menu.wait_until_location_stable()
        self.lnk_visa_quota_approval_side_menu.click()
