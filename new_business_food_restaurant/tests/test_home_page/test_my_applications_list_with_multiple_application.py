import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.ManageApplicationPage import ManageApplicationPage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage


class TestManageApplicationWithMultipleApplicationPage:

    @pytest.mark.smoke
    def test_manage_application_with_multiple_application_page(self):
        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_manage_application_page()

        """Login Page"""

        NavigateSteps.go_to_login_with_user1()

        """Manage Application Page"""

        with allure.step("Verify Manage Application Page"):
            manage_aplication = ManageApplicationPage()
            assert_that(manage_aplication.is_active_text_present(), "Active text is not displayed")



