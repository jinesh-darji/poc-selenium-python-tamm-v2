from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class CommercialLicensePage(BasePage):

    page_name = "Commercial License Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "commercial_license_locator")
    lnk_home = Link(locator_reader, "lnk_home")
    btn_start_activities = Button(locator_reader, "btn_start_activities")
    btn_start_legal_form = Button(locator_reader, "btn_start_legal_form")
    btn_start_trade_name = Button(locator_reader, "btn_start_trade_name")
    btn_start_document = Button(locator_reader, "btn_start_document")
    btn_start_payment_and_issuance = Button(locator_reader, "btn_start_payment_and_issuance")
    btn_side_menu_commercial_activities = Button(locator_reader, "btn_side_menu_commercial_activities")
    btn_side_menu_legal_form = Button(locator_reader, "btn_side_menu_legal_form")
    btn_side_menu_trade_name = Button(locator_reader, "btn_side_menu_trade_name")
    btn_side_menu_documents = Button(locator_reader, "btn_side_menu_documents")
    btn_side_menu_payment_and_issuance = Button(locator_reader, "btn_side_menu_payment_and_issuance")
    btn_commercial_activity_tab = Button(locator_reader, "btn_commercial_activity_tab")
    btn_legal_form_tab = Button(locator_reader, "btn_legal_form_tab")
    btn_trade_name_tab = Button(locator_reader, "btn_trade_name_tab")
    btn_documents_tab = Button(locator_reader, "btn_documents_tab")
    btn_payment_issuance_tab = Button(locator_reader, "btn_payment_issuance_tab")
    btn_view_details_trade_name = Button(locator_reader, "btn_view_details_trade_name")

    def __init__(self):
        super(CommercialLicensePage, self).__init__(self.page_element)

    def click_home_link(self):
        self.lnk_home.wait_until_location_stable()
        self.lnk_home.click()

    def click_activities_start_btn(self):
        self.btn_start_activities.wait_until_location_stable()
        self.btn_start_activities.click()

    def click_legal_form_start_btn(self):
        self.btn_start_legal_form.wait_until_location_stable()
        self.btn_start_legal_form.click()

    def click_trade_name_start_btn(self):
        self.btn_start_trade_name.wait_until_location_stable()
        self.btn_start_trade_name.click()

    def click_document_start_btn(self):
        self.btn_start_document.wait_until_location_stable()
        self.btn_start_document.click()

    def click_payment_and_issuance_start_btn(self):
        self.btn_start_payment_and_issuance.wait_until_location_stable()
        self.btn_start_payment_and_issuance.click()

    def click_side_menu_commercial_activities_btn(self):
        self.btn_side_menu_commercial_activities.wait_until_location_stable()
        self.btn_side_menu_commercial_activities.click()

    def click_side_menu_legal_form_btn(self):
        self.btn_side_menu_legal_form.wait_until_location_stable()
        self.btn_side_menu_legal_form.click()

    def click_side_menu_trade_name_btn(self):
        self.btn_side_menu_trade_name.wait_until_location_stable()
        self.btn_side_menu_trade_name.click()

    def click_side_menu_documents_btn(self):
        self.btn_side_menu_documents.wait_until_location_stable()
        self.btn_side_menu_documents.click()

    def click_side_menu_payment_and_issuance_btn(self):
        self.btn_side_menu_payment_and_issuance.wait_until_location_stable()
        self.btn_side_menu_payment_and_issuance.click()

    def click_commercial_license_tab(self):
        self.btn_commercial_activity_tab.wait_until_location_stable()
        self.btn_commercial_activity_tab.click()

    def click_btn_legal_form_tab(self):
        self.btn_legal_form_tab.wait_until_location_stable()
        self.btn_legal_form_tab.click()

    def click_btn_trade_name_tab(self):
        self.btn_trade_name_tab.wait_until_location_stable()
        self.btn_trade_name_tab.click()

    def click_btn_documents_tab(self):
        self.btn_documents_tab.wait_until_location_stable()
        self.btn_documents_tab.click()

    def click_btn_payment_issuance_tab(self):
        self.btn_payment_issuance_tab.wait_until_location_stable()
        self.btn_payment_issuance_tab.click()

    def click_btn_view_details_trade_name(self):
        self.btn_view_details_trade_name.wait_until_location_stable()
        self.btn_view_details_trade_name.click()


