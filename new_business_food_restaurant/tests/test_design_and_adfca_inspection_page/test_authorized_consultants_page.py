import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.DesignAndADFCAInspectionPage import DesignAndADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.AuthorizedConsultantsPage import AuthorizedConsultantsPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.DesignAndFitoutsPage import DesignAndFitoutsPage


class TestAuthorizedConsultantsPage:

    @pytest.mark.smoke
    def test_authorized_consultants_page(self):

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
            design_adfca.click_design_and_fitouts_btn()

        """Design and Out-fit Page"""

        with allure.step("Select 'Search Consultant' button"):
            design_fitout = DesignAndFitoutsPage()
            design_fitout.click_search_contractors_btn()

        """Authorized Consultants Page"""

        with allure.step("Select 'Search Consultant' button"):
            consultants = AuthorizedConsultantsPage()
            assert_that(consultants.is_consultants_detail_is_displayed(), "List of Consultants is not displayed")






