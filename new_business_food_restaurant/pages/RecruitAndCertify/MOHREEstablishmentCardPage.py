from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class MOHREEstablishmentCardPage(BasePage):
    page_name = "MOHRE Establishment Card Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "mohre_establishment_card_locator")
    lbl_mohre_establishment_card_text = Label(locator_reader, "lbl_mohre_establishment_card_text")

    def __init__(self):
        super(MOHREEstablishmentCardPage, self).__init__(self.page_element)

    def is_mohre_establishment_card_text_is_present(self):
        self.lbl_mohre_establishment_card_text.wait_until_location_stable()
        return self.lbl_mohre_establishment_card_text.is_present() and self.lbl_mohre_establishment_card_text.is_displayed()
