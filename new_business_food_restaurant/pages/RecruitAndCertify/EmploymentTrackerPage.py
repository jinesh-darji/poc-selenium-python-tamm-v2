from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.elements.Link import Link
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class EmploymentTrackerPage(BasePage):
    page_name = "Employment Tracker Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "employment_tracker_locator")
    btn_add_employee = Button(locator_reader, "btn_add_employee")
    lnk_recruit_and_certify = Link(locator_reader, "lnk_recruit_and_certify")
    lbl_employee_profile = Label(locator_reader, "lbl_employee_profile")
    lbl_moi = Label(locator_reader, "lbl_moi")

    def __init__(self):
        super(EmploymentTrackerPage, self).__init__(self.page_element)

    def click_add_employee_btn(self):
        self.btn_add_employee.wait_until_location_stable()
        self.btn_add_employee.click()

    def click_recruit_and_certify_link(self):
        self.lnk_recruit_and_certify.wait_until_location_stable()
        self.lnk_recruit_and_certify.click()

    def is_employee_profile_label_present(self):
        self.lbl_employee_profile.wait_until_location_stable()
        return self.lbl_employee_profile.is_displayed() and self.lbl_employee_profile.is_present()

    def is_lbl_moi_is_present(self):
        self.lbl_moi.wait_until_location_stable()
        return self.lbl_moi.is_present() and self.lbl_moi.is_displayed()
