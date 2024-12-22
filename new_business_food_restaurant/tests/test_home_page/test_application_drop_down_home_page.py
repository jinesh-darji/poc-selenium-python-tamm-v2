import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.LandingPage.RetaurantName import RestaurantNamePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicensePage import CommercialLicensePage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage


class TestApplicationDropDownHomePage:

    @pytest.mark.smoke
    def test_application_drop_down_home_page(self):

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_start_new_restaurant_page()

        """Home Page"""

        with allure.step("Select 'Start' button of 'commercial license'"):
            home = HomePage()
            home.click_commercial_license_start_btn()

        """Login Page"""

        NavigateSteps.go_to_login_with_user1()

        """Restaurant Name Page"""

        with allure.step("Enter restaurant name"):
            restaurant_name = RestaurantNamePage()
            restaurant_name.fill_restaurant_name()

        with allure.step("Select 'Start' button of 'Restaurant Name' page"):
            restaurant_name.click_start_btn()

        """Commercial License Page"""

        commerciallicense = CommercialLicensePage()
        commerciallicense.click_home_link()

        """Home Page"""

        with allure.step("Select 'Application' from my application drop down"):
            home.select_application("fff")

        with allure.step("Select 'Start' button of Discover"):
            home.click_discover_start_btn()

