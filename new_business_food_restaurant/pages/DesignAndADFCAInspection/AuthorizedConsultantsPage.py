from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AuthorizedConsultantsPage(BasePage):
    page_name = "Authorized Consultants Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "authorized_consultants_locator")
    lbl_consultants_detail = Label(locator_reader, "lbl_consultants_detail")

    def __init__(self):
        super(AuthorizedConsultantsPage, self).__init__(self.page_element)

    def is_consultants_detail_is_displayed(self):
        self.lbl_consultants_detail.try_wait_for_absent()
        self.lbl_consultants_detail.wait_for_is_present()
        return self.lbl_consultants_detail.is_present() and self.lbl_consultants_detail.is_displayed()




