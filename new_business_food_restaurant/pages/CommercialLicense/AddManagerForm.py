from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.InputDropdown import InputDropdown
from framework.elements.TextBox import TextBox
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader
from framework.forms.BaseForm import BaseForm


class AddManagerForm(BaseForm):
    form_name = "Add Manager Form"
    locator_reader = LocatorReader(form_name)
    page_element = Label(locator_reader, "add_manager_locator")
    drpdwn_title = InputDropdown(locator_reader, "drpdwn_title", "drpdwn_arrow_title", "txt_title")
    txb_name_in_english = TextBox(locator_reader, "txb_name_in_english")
    txb_name_in_arabic = TextBox(locator_reader, "txb_name_in_arabic")
    txb_emirati_id = TextBox(locator_reader, "txb_emirati_id")
    txb_email = TextBox(locator_reader, "txb_email")
    txb_phone_number = TextBox(locator_reader, "txb_phone_number")
    txb_passport_number = TextBox(locator_reader, "txb_passport_number")
    txb_pobox = TextBox(locator_reader, "txb_pobox")
    drpdwn_year_manager = InputDropdown(locator_reader, "drpdwn_year_manager", "arrow_year_number", "txt_year_number")
    txb_emirates = TextBox(locator_reader, "txb_emirates")
    txb_city = TextBox(locator_reader, "txb_city")
    txb_area = TextBox(locator_reader, "txb_area")
    txb_street = TextBox(locator_reader, "txb_street")
    txb_building = TextBox(locator_reader, "txb_building")
    txb_flat = TextBox(locator_reader, "txb_flat")
    btn_add_manager = Button(locator_reader, "btn_add_manager")

    def __init__(self):
        super(AddManagerForm, self).__init__(self.page_element)

    def drpdwn_select_title(self, title):
        self.drpdwn_title.wait_until_location_stable()
        self.drpdwn_title.open_dropdown()
        self.drpdwn_title.select_value(title)

    def fill_name_in_english(self):
        for element in self.txb_name_in_english.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_name_in_english"))

    def fill_name_in_arabic(self):
        for element in self.txb_name_in_arabic.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_name_in_arabic"))

    def fill_emirati_id(self):
        for element in self.txb_emirati_id.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_emirati_id"))

    def fill_email(self):
        for element in self.txb_email.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_email"))

    def fill_phone_number(self):
        for element in self.txb_phone_number.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_phone_number"))

    def fill_passport_number(self):
        for element in self.txb_passport_number.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txt_passport_number"))

    def fill_pobox(self):
        for element in self.txb_pobox.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_pobox"))

    def drpdwn_year_number(self, year):
        self.drpdwn_year_manager.wait_until_location_stable()
        self.drpdwn_year_manager.open_dropdown()
        self.drpdwn_year_manager.select_value(year)

    def fill_emirates(self):
        for element in self.txb_emirates.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_emirates"))

    def fill_city(self):
        for element in self.txb_city.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_city"))

    def fill_area(self):
        for element in self.txb_area.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_area"))

    def fill_street(self):
        for element in self.txb_street.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_street"))

    def fill_building(self):
        for element in self.txb_building.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_building"))

    def fill_flat(self):
        for element in self.txb_flat.get_elements():
            element.send_keys(DataReader.get_data("add_manager.txb_flat"))

    def click_submit_btn(self):
        self.btn_add_manager.click()
