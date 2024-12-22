from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.elements.Link import Link
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class EmployeeStepsPage(BasePage):
    page_name = "Employee Steps Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "employee_steps_locator")
    txb_moi_unified_number = TextBox(locator_reader, "txb_moi_unified_number")
    btn_submit = Button(locator_reader, "btn_submit")
    lnk_recruit_and_certify = Link(locator_reader, "lnk_recruit_and_certify")

    def __init__(self):
        super(EmployeeStepsPage, self).__init__(self.page_element)

    def fill_moi_unified_number(self):
        for element in self.txb_moi_unified_number.get_elements():
            element.send_keys(DataReader.get_data("employee_moi_number.moi_number"))

    def click_submit_btn(self):
        self.btn_submit.wait_until_location_stable()
        self.btn_submit.click()

    def click_recruit_and_certify_link(self):
        self.lnk_recruit_and_certify.wait_until_location_stable()
        self.lnk_recruit_and_certify.click()

