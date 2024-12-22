import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.LandingPage.PROFormPage import PROFormPage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.RetaurantName import RestaurantNamePage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage


class TestAssignPROPage:

    @pytest.mark.smoke
    def test_assign_pro_page(self):

        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_start_new_restaurant_page()

        """Home Page"""

        with allure.step("Select 'PRO' button"):
            home = HomePage()
            home.click_pro_btn()

        """Login Page"""

        NavigateSteps.go_to_login_with_user2()

        """Restaurant Name Page"""

        with allure.step("Enter restaurant name"):
            restaurant_name = RestaurantNamePage()
            restaurant_name.fill_restaurant_name()

        with allure.step("Select 'Start' button of 'Restaurant Name' page"):
            restaurant_name.click_start_btn()

        """Home Page"""

        home.click_pro_btn()

        """PRO Form"""

        with allure.step("Fill 'Name in English' text field"):
            form_field = PROFormPage()
            form_field.fill_name_english()

        with allure.step("Fill 'Name in Arabic' text field"):
            form_field.fill_name_arabic()

        with allure.step("Fill 'Name Emirate ID' text field"):
            form_field.fill_emirati_id()

        with allure.step("Fill 'Email Address' text field"):
            form_field.fill_email()

        with allure.step("Fill 'Phone Number' text field"):
            form_field.fill_phone_number()

        with allure.step("Select 'Assign PRO' button"):
            form_field.click_assign_pro_btn()


