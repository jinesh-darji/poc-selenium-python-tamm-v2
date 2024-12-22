from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.elements.Button import Button
from framework.utils.LocatorReader import LocatorReader


class GetFinancingPage(BasePage):
    page_name = "Get Financing Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "get_financing_locator")
    lbl_banks = Label(locator_reader, "lbl_banks")
    lbl_khalifa_fund = Label(locator_reader, "lbl_khalifa_fund")
    btn_bank_find_out_more = Button(locator_reader, "btn_bank_find_out_more")
    btn_khalifa_fund_find_out_more = Button(locator_reader, "btn_khalifa_fund_find_out_more")

    def __init__(self):
        super(GetFinancingPage, self).__init__(self.page_element)

    def is_banks_present(self):
        self.lbl_banks.wait_until_location_stable()
        return self.lbl_banks.is_displayed() and self.lbl_banks.is_present()

    def is_khalifa_fund_present(self):
        self.lbl_khalifa_fund.wait_until_location_stable()
        return self.lbl_khalifa_fund.is_present() and self.lbl_khalifa_fund.is_displayed()

    def click_find_out_more_bank_btn(self):
        self.btn_bank_find_out_more.wait_until_location_stable()
        self.btn_bank_find_out_more.click()

    def click_find_out_more_khalifa_fund_btn(self):
        self.btn_khalifa_fund_find_out_more.wait_until_location_stable()
        self.btn_khalifa_fund_find_out_more.click()
