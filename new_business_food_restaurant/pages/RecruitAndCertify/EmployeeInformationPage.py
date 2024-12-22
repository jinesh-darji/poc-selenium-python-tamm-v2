from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.elements.List import List
from framework.elements.TextBox import TextBox
from framework.elements.InputDropdown import InputDropdown
from framework.elements.Dropdown import Dropdown
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class EmploymentInformationPage(BasePage):
    page_name = "Employment Information Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "employment_information_locator")
    txb_first_name = TextBox(locator_reader, "txb_first_name")
    txb_last_name = TextBox(locator_reader, "txb_last_name")
    drpdwn_nationality = InputDropdown(locator_reader, "drop_down_nationality", "arrow_nationality",
                                          "txb_nationality")
    txb_passport_number = TextBox(locator_reader, "txb_passport_number")
    drpdwn_role = Dropdown(locator_reader, "drop_down_role", "arrow_role")
    item_drop_down_role = Label(locator_reader, "item_drop_down_role")
    lst_item_drop_down_role = List(locator_reader, "lst_item_drop_down_role")
    btn_add_employee = Button(locator_reader, "btn_add_employee")

    def __init__(self):
        super(EmploymentInformationPage, self).__init__(self.page_element)

    def fill_first_name(self):
        self.txb_first_name.wait_until_location_stable()
        for element in self.txb_first_name.get_elements():
            element.send_keys(DataReader.get_data("employee_information.first_name"))

    def fill_last_name(self):
        self.txb_last_name.wait_until_location_stable()
        for element in self.txb_last_name.get_elements():
            element.send_keys(DataReader.get_data("employee_information.last_name"))

    def select_nationality(self, nationality):
        self.drpdwn_nationality.wait_until_location_stable()
        self.drpdwn_nationality.open_dropdown()
        self.drpdwn_nationality.select_value(nationality)

    def fill_passport_number(self):
        self.txb_passport_number.wait_until_location_stable()
        for element in self.txb_passport_number.get_elements():
            element.send_keys(DataReader.get_data("employee_information.passport_number"))

    def select_role_drop_down(self):
        self.drpdwn_role.wait_until_location_stable()
        self.drpdwn_role.return_and_click_random_data_drpdwn(self.drpdwn_role, self.item_drop_down_role,
                                                                self.lst_item_drop_down_role)

    def click_add_employee_btn(self):
        self.btn_add_employee.wait_until_location_stable()
        self.btn_add_employee.click()
