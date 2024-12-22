from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class SummaryOfCommercialLicensePage(BasePage):
    page_name = "Summary Of Commercial License Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "summary_of_commercial_license_locator")
    btn_rent_yes = Button(locator_reader, "btn_rent_yes")
    btn_rent_no = Button(locator_reader, "btn_rent_no")
    txb_tawtheeq_number = TextBox(locator_reader, "txb_tawtheeq_number")
    btn_submit_your_application = Button(locator_reader, "btn_submit_your_application")

    def __init__(self):
        super(SummaryOfCommercialLicensePage, self).__init__(self.page_element)

    def click_rent_yes_radio(self):
        self.btn_rent_yes.try_wait_for_absent()
        self.btn_rent_yes.wait_for_is_present()
        self.btn_rent_yes.click()

    def click_rent_no_radio(self):
        self.btn_rent_no.try_wait_for_absent()
        self.btn_rent_no.wait_for_is_present()
        self.btn_rent_no.click()

    def fill_tawtheeq_number(self):
        self.txb_tawtheeq_number.wait_until_location_stable()
        self.txb_tawtheeq_number.send_keys(DataReader.get_data("cl_tawtheeq_number.tawtheeq_number"))

    def click_submit_your_application(self):
        self.btn_submit_your_application.wait_until_location_stable()
        self.btn_submit_your_application.click()
