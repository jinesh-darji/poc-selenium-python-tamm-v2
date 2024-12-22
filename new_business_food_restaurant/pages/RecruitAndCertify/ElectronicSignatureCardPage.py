from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ElectronicSignatureCardPage(BasePage):
    page_name = "Electronic Signature Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "electronic_signature_card_locator")
    lbl_electronic_signature_card_text = Label(locator_reader, "lbl_electronic_signature_card_text")

    def __init__(self):
        super(ElectronicSignatureCardPage, self).__init__(self.page_element)

    def is_electronic_signature_card_text_is_present(self):
        self.lbl_electronic_signature_card_text.wait_until_location_stable()
        return self.lbl_electronic_signature_card_text.is_present() and self.lbl_electronic_signature_card_text.is_displayed()
