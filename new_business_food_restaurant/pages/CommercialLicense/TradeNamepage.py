from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TradeNamePage(BasePage):
    page_name = "Trade Name Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "trade_name_locator")
    btn_trade_name_start = Button(locator_reader, 'btn_trade_name_start')
    btn_payment_start = Button(locator_reader, 'btn_payment_start')
    btn_initial_approval_start = Button(locator_reader, 'btn_initial_approval_start')
    btn_select_trade_name_open = Button(locator_reader, 'btn_select_trade_name_open')
    btn_ded_approval_open = Button(locator_reader, 'btn_ded_approval_open')
    btn_payment_open = Button(locator_reader, 'btn_payment_open')
    btn_initial_approval_open = Button(locator_reader, 'btn_initial_approval_open')
    btn_issued_commercial_license = Button(locator_reader, "btn_issued_commercial_license")

    def __init__(self):
        super(TradeNamePage, self).__init__(self.page_element)

    def click_select_trade_name_tab(self):
        self.btn_select_trade_name_open.try_wait_for_absent()
        self.btn_select_trade_name_open.wait_for_is_present()
        self.btn_select_trade_name_open.click()

    def click_select_trade_name_start(self):
        self.btn_trade_name_start.wait_until_location_stable()
        self.btn_trade_name_start.click()

    def click_ded_approval_open_tab(self):
        self.btn_ded_approval_open.try_wait_for_absent()
        self.btn_ded_approval_open.wait_for_is_present()
        self.btn_ded_approval_open.click()

    def click_payment_open_tab(self):
        self.btn_payment_open.try_wait_for_absent()
        self.btn_payment_open.wait_for_is_present()
        self.btn_payment_open.click()

    def click_payment_start(self):
        self.btn_payment_start.wait_until_location_stable()
        self.btn_payment_start.click()

    def click_initial_approval_tab(self):
        self.btn_initial_approval_open.try_wait_for_absent()
        self.btn_initial_approval_open.wait_for_is_present()
        self.btn_initial_approval_open.click()

    def click_initial_approval_start(self):
        self.btn_initial_approval_start.wait_until_location_stable()
        self.btn_initial_approval_start.click()

    def click_btn_issued_commercial_license(self):
        self.btn_issued_commercial_license.wait_until_location_stable()
        self.btn_issued_commercial_license.click()




