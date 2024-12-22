from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EntryPermitPage(BasePage):
    page_name = "Entry Permit Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "entry_permit_locator")
    lbl_entry_permit_text = Label(locator_reader, "lbl_entry_permit_text")

    def __init__(self):
        super(EntryPermitPage, self).__init__(self.page_element)

    def is_entry_permit_text_is_present(self):
        self.lbl_entry_permit_text.wait_until_location_stable()
        return self.lbl_entry_permit_text.is_present() and self.lbl_entry_permit_text.is_displayed()
