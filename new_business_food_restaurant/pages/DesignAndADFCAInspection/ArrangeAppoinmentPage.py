from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ArrangeAppointmentPage(BasePage):
    page_name = "Arrange Appointment Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "arrange_appointment_locator")
    lnk_design_and_adfca_inspection = Link(locator_reader, "lnk_design_and_adfca_inspection")
    btn_back_to_application = Button(locator_reader, "btn_back_to_application")
    btn_download_adfca = Button(locator_reader, "btn_download_adfca")

    def __init__(self):
        super(ArrangeAppointmentPage, self).__init__(self.page_element)

    def click_design_and_adfca_inspection_link(self):
        self.lnk_design_and_adfca_inspection.try_wait_for_absent()
        self.lnk_design_and_adfca_inspection.wait_for_is_present()
        self.lnk_design_and_adfca_inspection.click()

    def click_back_to_application_btn(self):
        self.btn_back_to_application.try_wait_for_absent()
        self.btn_back_to_application.wait_for_is_present()
        self.btn_back_to_application.click()

    def click_download_btn(self):
        self.btn_download_adfca.try_wait_for_absent()
        self.btn_download_adfca.wait_for_is_present()
        self.btn_download_adfca.click()


