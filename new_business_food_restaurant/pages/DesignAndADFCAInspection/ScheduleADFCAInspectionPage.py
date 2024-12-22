from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ScheduleADFCAInspectionPage(BasePage):
    page_name = "Schedule ADFCA Inspection Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "schedule_adfca_inspection_locator")
    btn_submit_request = Button(locator_reader, "btn_submit_request")

    def __init__(self):
        super(ScheduleADFCAInspectionPage, self).__init__(self.page_element)

    def click_submit_request_btn(self):
        self.btn_submit_request.try_wait_for_absent()
        self.btn_submit_request.wait_for_is_present()
        self.btn_submit_request.click()


