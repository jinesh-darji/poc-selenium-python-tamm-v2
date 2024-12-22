from framework.elements.Button import Button
from framework.elements.TextBox import TextBox
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class CreateMOAPage(BasePage):
    page_name = "Create MOA Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "create_moa_locator")
    txb_total_capital = TextBox(locator_reader, "txb_total_capital")
    txb_annual_revenue = TextBox(locator_reader, "txb_annual_revenue")
    txb_total_number_of_shares = TextBox(locator_reader, "txb_total_number_of_shares")
    btn_add_manager = Button(locator_reader, "btn_add_manager")
    btn_submit = Button(locator_reader, "btn_submit")

    def __init__(self):
        super(CreateMOAPage, self).__init__(self.page_element)

    def fill_total_capital(self):
        for element in self.txb_total_capital.get_elements():
            element.send_keys(DataReader.get_data("create_moa.txb_total_capital"))

    def fill_annual_revenue(self):
        for element in self.txb_annual_revenue.get_elements():
            element.send_keys(DataReader.get_data("create_moa.txb_annual_revenue"))

    def fill_total_number_of_shares(self):
        for element in self.txb_total_number_of_shares.get_elements():
            element.send_keys(DataReader.get_data("create_moa.txb_total_number_of_shares"))

    def click_add_manager_btn(self):
        self.btn_add_manager.wait_until_location_stable()
        self.btn_add_manager.click()

    def click_submit_btn(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()



