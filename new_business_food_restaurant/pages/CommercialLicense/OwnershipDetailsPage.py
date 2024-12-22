from framework.elements.Button import Button
from framework.elements.Slider import Slider
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class OwnershipDetailsPage(BasePage):
    page_name = "Ownership Details Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "ownership_details_locator")
    btn_add_sponsor = Button(locator_reader, "btn_add_sponsor")
    btn_add_partner = Button(locator_reader, "btn_add_partner")
    sld_partner = Slider(locator_reader, "sld_partner")
    btn_next = Button(locator_reader, "btn_next")

    def __init__(self):
        super(OwnershipDetailsPage, self).__init__(self.page_element)

    def click_add_sponsor_btn(self):
        self.btn_add_sponsor.try_wait_for_absent()
        self.btn_add_sponsor.wait_for_is_present()
        self.btn_add_sponsor.click()

    def click_add_partner_btn(self):
        self.btn_add_partner.try_wait_for_absent()
        self.btn_add_partner.wait_for_is_present()
        self.btn_add_partner.click()

    def click_partner_slider(self):
        self.sld_partner.try_wait_for_absent()
        self.sld_partner.wait_for_is_present()
        self.sld_partner.click_on_slider(2)

    def click_next_btn(self):
        self.btn_next.try_wait_for_absent()
        self.btn_next.wait_for_is_present()
        self.btn_next.click()


