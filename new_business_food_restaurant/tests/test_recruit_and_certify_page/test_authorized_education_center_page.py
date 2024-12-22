import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.RecruitAndCertify.RecruitAndCertifyPage import RecruitAndCertifyPage
from new_business_food_restaurant.pages.RecruitAndCertify.AuthorizedEducationCenterPage import \
    AuthorizedEducationCenterPage


class TestAuthorizedEducationCenterPage:

    @pytest.mark.smoke
    def test_authorized_education_center_page(self):

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

        with allure.step("Select 'Certify' button"):
            recruit_certify = RecruitAndCertifyPage()
            recruit_certify.click_certification_btn()

        """Certify Page"""

        with allure.step("Verify 'Authorized Education Centers' list"):
            center_list = AuthorizedEducationCenterPage()
            center_list.is_center_name_present()

