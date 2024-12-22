from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class SummaryOfLegalFormPage(BasePage):
    page_name = "Summary of Legal Form Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_of_legal_form_locator")
    btn_select_trade_name = Button(locator_reader, "btn_select_trade_name")
    lnk_reselect_legal_form = Link(locator_reader, "lnk_reselect_legal_form")

    def __init__(self):
        super(SummaryOfLegalFormPage, self).__init__(self.page_element)

    def click_select_trade_name(self):
        self.btn_select_trade_name.click()

    def click_reselect_legal_form_link(self):
        self.lnk_reselect_legal_form.click()

