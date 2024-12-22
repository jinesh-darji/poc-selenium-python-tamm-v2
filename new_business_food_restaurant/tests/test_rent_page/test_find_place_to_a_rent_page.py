import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.Rent.RentPage import RentPage
from new_business_food_restaurant.pages.Rent.FindPlacePage import FindPlacePage


class TestFindPlaceToARentPage:

    @pytest.mark.smoke
    def test_find_place_to_a_rent_page(self):

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
            rent_page.click_find_place_btn()

        """Place of a Rent Page"""

        with allure.step("is 'Propertyfinder' text is displayed"):
            find_place = FindPlacePage()
            assert_that(find_place.is_property_finder_present(), "is 'Propertyfinder' text is not displayed")

        with allure.step("is 'bayut' text is displayed"):
            assert_that(find_place.is_bayut_present(), "is 'bayut' text is not displayed")

        with allure.step("is 'dubizzle' text is displayed"):
            assert_that(find_place.is_dubizzle_present(), "is 'dubizzle' text is displayed")
