from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class AuthorizedContractorsPage(BasePage):
    page_name = "Authorized Contractors Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "authorized_contractors_locator")
    lbl_contractors_detail = Label(locator_reader, "lbl_contractors_detail")

    def __init__(self):
        super(AuthorizedContractorsPage, self).__init__(self.page_element)

    def is_displayed_contractors_detail(self):
        self.lbl_contractors_detail.try_wait_for_absent()
        self.lbl_contractors_detail.wait_for_is_present()
        return self.lbl_contractors_detail.is_present() and self.lbl_contractors_detail.is_displayed()


