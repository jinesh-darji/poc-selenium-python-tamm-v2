from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.TextBox import TextBox
from framework.elements.Calendar import Calendar
from framework.forms.BaseForm import BaseForm
from framework.utils.LocatorReader import LocatorReader
from framework.utils.DataReader import DataReader


class AddSponsorForm(BaseForm):
    form_name = "Add Sponsor Form"
    locator_reader = LocatorReader(form_name)
    page_element = Label(locator_reader, "add_sponsor_locator")
    txb_name_in_english = TextBox(locator_reader, "txb_name_in_english")
    txb_name_in_arabic = TextBox(locator_reader, "txb_name_in_arabic")
    dob_datepicker = Calendar(locator_reader, "dob_datepicker", "btn_today", "btn_previous_month", "btn_day")
    txb_emirati_id = TextBox(locator_reader, "txb_emirati_id")
    txb_email = TextBox(locator_reader, "txb_email")
    txb_phone_number = TextBox(locator_reader, "txb_phone_number")
    txb_emirates = TextBox(locator_reader, "txb_emirates")
    txb_city = TextBox(locator_reader, "txb_city")
    txb_area = TextBox(locator_reader, "txb_area")
    txb_street = TextBox(locator_reader, "txb_street")
    txb_building = TextBox(locator_reader, "txb_building")
    btn_submit = Button(locator_reader, "btn_submit")

    def __init__(self):
        super(AddSponsorForm, self).__init__(self.page_element)

    def fill_name_in_english(self):
        for element in self.txb_name_in_english.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_name_in_english"))

    def fill_name_in_arabic(self):
        for element in self.txb_name_in_arabic.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_name_in_english"))

    def set_dob_date(self):
        self.dob_datepicker.set_today_date()

    def fill_emirati_id(self):
        for element in self.txb_emirati_id.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_emirati_id"))

    def fill_email(self):
        for element in self.txb_email.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_email"))

    def fill_phone_number(self):
        for element in self.txb_phone_number.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_phone_number"))

    def fill_emirates(self):
        for element in self.txb_emirates.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_emirates"))

    def fill_city(self):
        for element in self.txb_city.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_city"))

    def fill_area(self):
        for element in self.txb_area.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_area"))

    def fill_street(self):
        for element in self.txb_street.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_street"))

    def fill_building(self):
        for element in self.txb_building.get_elements():
            element.send_keys(DataReader.get_data("add_sponsor.txb_building"))

    def click_submit_btn(self):
        self.btn_submit.click()
