import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.Rent.RentPage import RentPage
from new_business_food_restaurant.pages.Rent.ProvideTawtheeqNumberPage import ProvideTawtheeqNumberPage


class TestTawtheeqNumberAssignedToRestaurantPage:

    @pytest.mark.smoke
    def test_tawtheeq_number_assigned_to_restaurant_page(self):

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

        NavigateSteps.go_to_commercial_license_issued_without_rent_page()

        """Rent Page"""

        with allure.step("Select 'Provide Tawtheeq Number' button"):
            rent_page = RentPage()
            rent_page.click_provide_tawtheeq_number_btn()

        """Provide Tawtheeq Number Page"""

        with allure.step("Fill Tawtheeq Number in text fields"):
            provide_tawtheeqnumber = ProvideTawtheeqNumberPage()
            provide_tawtheeqnumber.fill_tawtheeq_number()

        with allure.step("Select 'Submit' button"):
            provide_tawtheeqnumber.click_submit_btn()

        with allure.step("is 'Registration Fee' is displayed"):
            assert_that(provide_tawtheeqnumber.is_registration_fee_is_present(),
                        "is 'Registration Fee' is not displayed")

        with allure.step("Select 'Payment' button"):
            provide_tawtheeqnumber.click_payment_btn()
