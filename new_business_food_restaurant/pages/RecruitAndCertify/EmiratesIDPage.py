from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EmiratesIDPage(BasePage):
    page_name = "Emirates ID Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "emirates_id_locator")
    lbl_emirates_id_text = Label(locator_reader, "lbl_emirates_id_text")

    def __init__(self):
        super(EmiratesIDPage, self).__init__(self.page_element)

    def is_emirates_id_text_is_present(self):
        self.lbl_emirates_id_text.wait_until_location_stable()
        return self.lbl_emirates_id_text.is_present() and self.lbl_emirates_id_text.is_displayed()
