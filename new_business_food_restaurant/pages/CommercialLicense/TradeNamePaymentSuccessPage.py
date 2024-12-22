from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TradeNamePaymentSuccessPage(BasePage):
    page_name = "Trade Name Payment Success Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "trade_name_payment_success_locator")
    lbl_tnnumber = Label(locator_reader, "lbl_tnnumber")
    lnk_commercial_license = Link(locator_reader, "lnk_commercial_license")

    def __init__(self):
        super(TradeNamePaymentSuccessPage, self).__init__(self.page_element)

    def is_success_text_present(self):
        self.lbl_tnnumber.wait_until_location_stable()
        return self.lbl_tnnumber.is_present() and self.lbl_tnnumber.is_displayed()

    def click_commercial_license_link(self):
        self.lnk_commercial_license.click()



