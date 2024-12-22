from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class TradeNameSuccessPage(BasePage):
    page_name = "Trade Name Success Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "trade_name_success_locator")
    btn_download = Button(locator_reader, "btn_download")
    btn_documents = Button(locator_reader, "btn_documents")

    def __init__(self):
        super(TradeNameSuccessPage, self).__init__(self.page_element)

    def click_download_btn(self):
        self.btn_download.wait_until_location_stable()
        self.btn_download.click()

    def click_documents_btn(self):
        self.btn_documents.try_wait_for_absent()
        self.btn_documents.wait_for_is_present()
        self.btn_documents.click()

