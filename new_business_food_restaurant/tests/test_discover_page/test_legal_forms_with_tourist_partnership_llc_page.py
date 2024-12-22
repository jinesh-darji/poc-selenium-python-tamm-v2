import pytest
import allure
from hamcrest import assert_that

from framework.browser.Browser import Browser
from new_business_food_restaurant.pages.Discover.DiscoverNeworBranchRestaurantPage import \
    DiscoverNeworBranchRestaurantPage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.Discover.DiscoverPage import DiscoverPage
from new_business_food_restaurant.pages.Discover.DiscoverServiceListPage import DiscoverServiceListPage
from new_business_food_restaurant.pages.Discover.DiscoverProvideMealPage import DiscoverProvideMealPage
from new_business_food_restaurant.pages.Discover.DiscoverDeliveryFoodPage import DiscoverDeliveryFoodPage
from new_business_food_restaurant.pages.Discover.AreaDetailsForm import AreaDetailsForm
from new_business_food_restaurant.pages.Discover.EmiratiPage import EmiratiPage
from new_business_food_restaurant.pages.Discover.GCCPage import GCCPage
from new_business_food_restaurant.pages.Discover.DiscoverSoleOrPartnershipPage import DiscoverSoleOrPartnershipPage
from new_business_food_restaurant.pages.Discover.DiscoverEstablishmentPage import DiscoverEstablishmentPage
from new_business_food_restaurant.pages.Discover.SizeOfRestaurantPage import SizeOfRestaurantPage
from new_business_food_restaurant.pages.Discover.EmployeeHirePage import EmployeeHirePage
from new_business_food_restaurant.pages.Discover.SummaryCostCalculatorPage import SummaryCostCalculatorPage

area_detail = \
    "https://journeys-demo.digitalx1.io/journeys/new-business-food-restaurant/discover/areas/Al%20Mushrif--ADM"


class TestLegalFormsWithTouristPartnershipLLCPage:

    @pytest.mark.smoke
    def test_legal_forms_with_tourist_partnership_llc_page(self):

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_start_new_restaurant_page()

        """Home Page"""

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

        with allure.step("Select 'Yes' button on 'Delivery Food' page"):
            delivery_food = DiscoverDeliveryFoodPage()
            delivery_food.click_yes_btn()

        with allure.step("Select 'Next' button on 'Provide Meal' page"):
            delivery_food.click_next_btn()

        """
        Area Details Page
        """
        with allure.step("Open pop up for area details"):
            browser = Browser()
            browser.set_url(area_detail)

        with allure.step("Select 'Business' tab of 'Area Detail' form"):
            area_details_form = AreaDetailsForm()
            area_details_form.click_business_tab_btn()

        with allure.step("Select 'Population' tab of 'Area Detail' form"):
            area_details_form.click_population_tab_btn()

        with allure.step("Select 'Trends' tab of 'Area Detail' form"):
            area_details_form.click_trends_tab()

        with allure.step("Select 'Next' button of 'Area Detail' form"):
            area_details_form.click_next_btn()

        """
        Emirati Page
        """
        with allure.step("Select 'No' button of 'Are you an emirati?' page"):
            emirati = EmiratiPage()
            emirati.click_no_btn()

        with allure.step("Select 'Next' button of 'Are you an emirati?' page"):
            emirati.click_next_btn()

        """
        GCC Page
        """
        with allure.step("Select 'No' button of 'Are you an GCC?' page"):
            gcc = GCCPage()
            gcc.click_yes_btn()

        with allure.step("Select 'Next' button of 'Are you an GCC?' page"):
            gcc.click_next_btn()

        """New Restaurant and UAE Branch"""

        with allure.step("Select 'UAE Branch' button"):
            discover_new_branch = DiscoverNeworBranchRestaurantPage()
            discover_new_branch.click_new_restaurant_btn()

        with allure.step("Select 'Next' button"):
            discover_new_branch.click_next_btn()

        """
        Sole and Partnership Page
        """
        with allure.step("Select 'Partnership' button of 'How will the company be formed?' page"):
            sole_partner = DiscoverSoleOrPartnershipPage()
            sole_partner.click_partnership_btn()

        with allure.step("Select 'Next' button of 'How will the company be formed?' page"):
            sole_partner.click_next_btn()

        """
        Establishment Page
        """
        with allure.step("Select 'LLC' button of 'You're eligible to establish the following:' page"):
            establishment = DiscoverEstablishmentPage()
            establishment.click_llc_btn()

        with allure.step("Select 'Next' button of 'You're eligible to establish the following:' page"):
            establishment.click_next_btn()

        """
        Size of restaurant Page
        """
        with allure.step("Mention 'Size of the restaurant' of 'What is the size of the restaurant?' page"):
            size_of_restaurant = SizeOfRestaurantPage()
            size_of_restaurant.click_size_of_restaurant_slider_btn()

        with allure.step("Select 'Next' button of 'What is the size of the restaurant?' page"):
            size_of_restaurant.click_next_btn()

        """
        Number of Employees Page
        """
        with allure.step("Mention 'Size of the restaurant' of 'How many employees are you looking to hire?' page"):
            employee_hire = EmployeeHirePage()
            employee_hire.fill_employee_count()

        with allure.step("Select 'Cost Calculator' button of 'How many employees are you looking to hire?' page"):
            employee_hire.click_next_btn()

        """
        Summary of Cost Calculator Page
        """
        with allure.step("Select 'Print' button"):
            cost_calculator = SummaryCostCalculatorPage()
            cost_calculator.click_print_btn()

        with allure.step("Select 'Commercial License' button of 'Summary of Cost Calculator' page"):
            cost_calculator = SummaryCostCalculatorPage()
            cost_calculator.click_commercial_license_btn()

