from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.forms.BaseForm import BaseForm
from framework.utils.LocatorReader import LocatorReader


class RemovePROForm(BaseForm):
    form_name = "Remove PRO Form"
    locator_reader = LocatorReader(form_name)
    page_element = Label(locator_reader, "remove_pro_locator")
    btn_cancel = Button(locator_reader, "btn_cancel")
    btn_confirm = Button(locator_reader, "btn_confirm")

    def __init__(self):
        super(RemovePROForm, self).__init__(self.page_element)

    def click_cancel_btn(self):
        self.btn_cancel.wait_until_location_stable()
        self.btn_cancel.click()

    def click_confirm_btn(self):
        self.btn_confirm.wait_until_location_stable()
        self.btn_confirm.click()
