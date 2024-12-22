from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class MOAReferenceNumberPage(BasePage):
    page_name = "MOA Reference Number Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "moa_reference_number_locator")
    txb_reference_number = TextBox(locator_reader, "txb_reference_number")
    btn_submit = Button(locator_reader, "btn_submit")

    def __init__(self):
        super(MOAReferenceNumberPage, self).__init__(self.page_element)

    def fill_reference_number(self):
        for element in self.txb_reference_number.get_elements():
            element.send_keys(DataReader.get_data("txb_reference_number.reference_number"))

    def click_btn_submit(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()






