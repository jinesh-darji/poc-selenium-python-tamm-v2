import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.ManageApplicationPage import ManageApplicationPage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage


class TestManageApplicationWithNoApplicationPage:

    @pytest.mark.smoke
    def test_manage_application_with_no_application_page(self):

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_manage_application_page()

        """Login Page"""

        NavigateSteps.go_to_login_with_user4()
        """Manage Application Page"""

        with allure.step("Verify Manage Application Page"):
            manage_aplication = ManageApplicationPage()
            assert_that(manage_aplication.is_no_restaurant_present(), "No Restaurant text is not displayed")



