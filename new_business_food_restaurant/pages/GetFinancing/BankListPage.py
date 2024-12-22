from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BankListPage(BasePage):
    page_name = "Bank List Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "bank_list_locator")
    lbl_bank_list = Label(locator_reader, "lbl_bank_list")

    def __init__(self):
        super(BankListPage, self).__init__(self.page_element)

    def is_bank_list_is_present(self):
        self.lbl_bank_list.wait_until_location_stable()
        return self.lbl_bank_list.is_displayed() and self.lbl_bank_list.is_present()
