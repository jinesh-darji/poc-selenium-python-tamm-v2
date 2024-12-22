import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.Login.LoginTAMMPage import LoginTAMMPage
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.RecruitAndCertify.EmployeeInformationPage import EmploymentInformationPage
from new_business_food_restaurant.pages.RecruitAndCertify.EmploymentTrackerPage import EmploymentTrackerPage
from new_business_food_restaurant.pages.RecruitAndCertify.RecruitAndCertifyPage import RecruitAndCertifyPage
from new_business_food_restaurant.pages.RecruitAndCertify.EmployeeStepsPage import EmployeeStepsPage


class TestMOIUnifiedNumberPage:

    @pytest.mark.smoke
    def test_moi_unified_number_page(self):

        """Commercial Activities"""

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_start_new_restaurant_page()

        with allure.step("Select 'Start' button of 'commercial license'"):
            home = HomePage()
            home.click_commercial_license_start_btn()

        """Login Page"""

        NavigateSteps.go_to_login_with_user2()

        """Navigate to Commercial License Page"""

        NavigateSteps.go_to_commercial_license_issued_page()

        """ADFCA Inspection Page"""

        with allure.step("Select 'Schedule an Inspection with ADFCA' button"):
            adfca_inspection = ADFCAInspectionPage()
            adfca_inspection.click_application_link()

        """Home Page"""

        with allure.step("Select 'start' button of recruitment"):
            home.click_recruit_and_certify_start_btn()

        """Recruit & Certify Page"""

        with allure.step("Select 'Employment Tracker' button"):
            recruit_certify = RecruitAndCertifyPage()
            recruit_certify.click_employment_tracker_btn()

        """Employee Tracker Page"""

        with allure.step("Select 'Employee Tracker' button"):
            employee_tracker = EmploymentTrackerPage()
            employee_tracker.click_add_employee_btn()

        """Employee Information page"""

        with allure.step("Fill 'First Name' field"):
            employee_information = EmploymentInformationPage()
            employee_information.fill_first_name()

        with allure.step("Fill 'Last Name' field"):
            employee_information.fill_last_name()

        with allure.step("Select 'Nationality' from the drop down"):
            employee_information.select_nationality("ALBANIA")

        with allure.step("Fill 'Passport' field"):
            employee_information.fill_passport_number()

        with allure.step("Select 'Role' from the drop down"):
            employee_information.select_role_drop_down()

        with allure.step("Click on 'Add Employee' button"):
            employee_information.click_add_employee_btn()

        """Employee Steps Page"""

        with allure.step("Fill MOI Number in text field"):
            employee_steps = EmployeeStepsPage()
            employee_steps.fill_moi_unified_number()

        with allure.step("Select 'Submit' button"):
            employee_steps.click_submit_btn()

        with allure.step("Click on 'Recruitment and Certify' link"):
            employee_steps.click_recruit_and_certify_link()

        """Employee and Certify Page"""

        with allure.step("Select 'Employee Tracker' button"):
            recruit_certify.click_employment_tracker_btn()

        """Employee Tracker Page"""

        with allure.step("is 'Employee Information' text displayed"):
            assert_that(employee_tracker.lbl_moi, "is 'Employee Information' text not displayed")


