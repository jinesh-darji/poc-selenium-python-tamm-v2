from framework.elements.Label import Label
from framework.elements.Button import Button
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class RecruitAndCertifyPage(BasePage):
    page_name = "Recruit And Certify Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "recruit_and_certify_locator")
    btn_registration = Button(locator_reader, "btn_registration")
    btn_recruitment = Button(locator_reader, "btn_recruitment")
    btn_employment_tracker = Button(locator_reader, "btn_employment_tracker")
    btn_certification = Button(locator_reader, "btn_certification")

    def __init__(self):
        super(RecruitAndCertifyPage, self).__init__(self.page_element)

    def click_registration_btn(self):
        self.btn_registration.wait_until_location_stable()
        self.btn_registration.click()

    def click_recruitment_btn(self):
        self.btn_recruitment.wait_until_location_stable()
        self.btn_recruitment.click()

    def click_employment_tracker_btn(self):
        self.btn_employment_tracker.try_wait_for_absent()
        self.btn_employment_tracker.wait_for_is_present()
        self.btn_employment_tracker.click()

    def click_certification_btn(self):
        self.btn_certification.wait_until_location_stable()
        self.btn_certification.click()


