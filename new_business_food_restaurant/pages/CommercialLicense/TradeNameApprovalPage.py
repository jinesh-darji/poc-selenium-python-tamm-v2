from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TradeNameApprovalPage(BasePage):
    page_name = "Trade Name Approval Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "trade_name_approval_locator")
    lnk_commercial_license = Link(locator_reader, "lnk_commercial_license")
    btn_next = Button(locator_reader, "btn_next")

    def __init__(self):
        super(TradeNameApprovalPage, self).__init__(self.page_element)

    def click_commercial_license_link(self):
        self.lnk_commercial_license.wait_until_location_stable()
        self.lnk_commercial_license.click()

    def click_next_btn(self):
        self.btn_next.try_wait_for_absent()
        self.btn_next.wait_for_is_present()
        self.btn_next.click()


