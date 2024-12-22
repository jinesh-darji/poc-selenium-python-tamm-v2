from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ManagePage(BasePage):
    page_name = "Manage Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "manage_locator")
    doe_lbl = Label(locator_reader, "lbl_doe")
    etisalat_lbl = Label(locator_reader, "lbl_etisalat")
    lnk_doe = Link(locator_reader, "lnk_doe")
    lnk_etisalat = Link(locator_reader, "lnk_etisalat")

    def __init__(self):
        super(ManagePage, self).__init__(self.page_element)

    def is_doe_lbl_displayed(self):
        self.doe_lbl.wait_until_location_stable()
        return self.doe_lbl.is_present() and self.is_doe_lbl.is_displayed()

    def is_doe_link_present(self):
        self.lnk_doe.wait_until_location_stable()
        return self.lnk_doe.is_displayed() and self.lnk_doe.is_present()

    def is_etisalat_lbl_displayed(self):
        self.etisalat_lbl.wait_until_location_stable()
        return self.etisalat_lbl.is_present() and self.is_etisalat_lbl.is_displayed()

    def is_etisalat_link_present(self):
        self.lnk_etisalat.wait_until_location_stable()
        return self.lnk_etisalat.is_displayed() and self.lnk_etisalat.is_present()
