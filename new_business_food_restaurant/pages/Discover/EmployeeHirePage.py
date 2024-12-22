from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.elements.TextBox import TextBox
from framework.utils.DataReader import DataReader
from framework.utils.LocatorReader import LocatorReader


class EmployeeHirePage(BasePage):
    page_name = "Employee Hire Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "employee_hire_locator")
    lbl_number_of_employee = Label(locator_reader, "lbl_number_of_employee")
    btn_next = Button(locator_reader, "btn_next")
    btn_previous = Button(locator_reader, "btn_previous")
    txb_employee_count = TextBox(locator_reader, "txb_employee_count")

    def __init__(self):
        super(EmployeeHirePage, self).__init__(self.page_element)

    def is_display_number_of_employee(self):
        self.lbl_number_of_employee.wait_until_location_stable()
        self.lbl_number_of_employee.click()

    def fill_employee_count(self):
        for element in self.txb_employee_count.get_elements():
            element.send_keys(DataReader.get_data("employee_count.employee"))

    def click_next_btn(self):
        self.btn_next.wait_until_location_stable()
        self.btn_next.click()

    def click_previous_btn(self):
        self.btn_previous.wait_until_location_stable()
        self.btn_previous.click()



