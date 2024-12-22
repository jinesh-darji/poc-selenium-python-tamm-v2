from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class WorkContractPage(BasePage):
    page_name = "Work Contract Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "work_contract_locator")
    lbl_work_contract_text = Label(locator_reader, "lbl_work_contract_text")

    def __init__(self):
        super(WorkContractPage, self).__init__(self.page_element)

    def is_work_contract_text_is_present(self):
        self.lbl_work_contract_text.wait_until_location_stable()
        return self.lbl_work_contract_text.is_present() and self.lbl_work_contract_text.is_displayed()
