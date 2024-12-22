from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ScheduledADFCAInspectionPage(BasePage):
    page_name = "Scheduled ADFCA Inspection Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "scheduled_adfca_inspection_locator")
    lbl_scheduled_adfca = Label(locator_reader, "lbl_scheduled_adfca")

    def __init__(self):
        super(ScheduledADFCAInspectionPage, self).__init__(self.page_element)

    def is_adfca_inspection_scheduled_is_displayed(self):
        self.lbl_scheduled_adfca.wait_until_location_stable()
        return self.lbl_scheduled_adfca.is_present() and self.lbl_scheduled_adfca.is_displayed()
