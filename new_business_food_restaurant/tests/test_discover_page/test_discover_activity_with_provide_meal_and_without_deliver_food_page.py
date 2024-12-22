import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.Discover.DiscoverPage import DiscoverPage
from new_business_food_restaurant.pages.Discover.DiscoverServiceListPage import DiscoverServiceListPage
from new_business_food_restaurant.pages.Discover.DiscoverDeliveryFoodPage import DiscoverDeliveryFoodPage
from new_business_food_restaurant.pages.Discover.DiscoverProvideMealPage import DiscoverProvideMealPage
from new_business_food_restaurant.pages.Discover.MapPage import MapPage


class TestDiscoverActivityWithProvideMealAndWithoutDeliverFoodPage:

    """Use can able to open activity page"""

    @pytest.mark.smoke
    def test_discover_activity_with_provide_meal_and_without_deliver_food_page(self):

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """ Home Grant page """

        NavigateSteps.go_to_start_new_restaurant_page()

        """ Home page """

        with allure.step("Select 'Discover Start' Button on 'Home' page"):
            home_page = HomePage()
            home_page.click_discover_start_btn()

        """ Home page of Discover """

        with allure.step("Select 'Get Start' Button on 'Discover' page"):
            discover_page = DiscoverPage()
            discover_page.click_get_started_btn()

        """ Service Listing Page """

        with allure.step("Select 'Bakery' button on 'Service List' page"):
            service_list = DiscoverServiceListPage()
            service_list.click_bakery_btn()

        with allure.step("Select 'Fast Food' button on 'Service List' page"):
            service_list.click_fast_food_btn()

        with allure.step("Select 'Next' button on 'Service List' page"):
            service_list.click_next_btn()

        """ Provide Meal Page """

        with allure.step("Select 'Yes' button on 'Provide Meal' page"):
            provide_meal = DiscoverProvideMealPage()
            provide_meal.click_yes_btn()

        with allure.step("Select 'Next' button on 'Provide Meal' page"):
            provide_meal.click_next_btn()

        """ Deliver Food Page """

        with allure.step("Select 'No' button on 'Delivery Food' page"):
            delivery_food = DiscoverDeliveryFoodPage()
            delivery_food.click_no_btn()

        with allure.step("Select 'Next' button on 'Provide Meal' page"):
            delivery_food.click_next_btn()

        """ Map Page"""

        with allure.step("Map instruction is displayed"):
            map = MapPage()
            assert_that(map.map_instruction_is_displayed(), "Map instruction is not displayed")



