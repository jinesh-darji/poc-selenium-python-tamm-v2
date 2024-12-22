import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.DesignAndADFCAInspectionPage import DesignAndADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ManagePage import ManagePage


class TestAuthorizedContractorsPage:

    @pytest.mark.smoke
    def test_authorized_contractors_page(self):

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
            adfca_inspection.click_design_adfca_inspection_link()

        """Design and ADFCA Inspection Page"""

        with allure.step("Select 'Design and Fit-out' button"):
            design_adfca = DesignAndADFCAInspectionPage()
            design_adfca.click_manage_btn()

        """Utilities Page"""

        with allure.step("EOD text is displayed"):
            manage = ManagePage()
            assert_that(manage.is_doe_lbl_displayed(), "EOD text is not displayed")

        with allure.step("EOD link is displayed"):
            assert_that(manage.is_doe_link_present(), "EOD link is not displayed")

        with allure.step("Etisalat text is displayed"):
            assert_that(manage.is_etisalat_lbl_displayed(), "Etisalat text is not displayed")

        with allure.step("Etisalat link is displayed"):
            assert_that(manage.is_etisalat_link_present(), "Etisalat link is not displayed")
