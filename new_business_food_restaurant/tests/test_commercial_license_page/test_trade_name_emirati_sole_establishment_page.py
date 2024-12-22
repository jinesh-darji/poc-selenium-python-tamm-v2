import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.LandingPage.RetaurantName import RestaurantNamePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicensePage import CommercialLicensePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseServiceListPage import CommercialLicenseServiceListPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseProvideMealPage import CommercialLicenseProvideMealPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseDeliveryFoodPage import CommercialLicenseDeliveryFoodPage
from new_business_food_restaurant.pages.CommercialLicense.SummaryOfActivitiesPage import SummaryOfActivitiesPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseSoleOrPartnershipPage import CommercialLicenseSoleOrPartnershipPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseEstablishmentPage import CommercialLicenseEstablishmentPage
from new_business_food_restaurant.pages.CommercialLicense.SummaryOfLegalFormPage import SummaryOfLegalFormPage
from new_business_food_restaurant.pages.CommercialLicense.TradeNamepage import TradeNamePage
from new_business_food_restaurant.pages.CommercialLicense.EnterTradeName import EnterTradeNamePage
from new_business_food_restaurant.pages.CommercialLicense.TradeNameApprovalPage import TradeNameApprovalPage
from new_business_food_restaurant.pages.Login.LoginTAMMPage import LoginTAMMPage


class TestTradNameEmiratiSoleEstablishmentPage:

    @pytest.mark.smoke
    def test_trade_name_emirati_sole_establishment_page(self):

        """Commercial Activities"""

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

        NavigateSteps.go_to_login_with_user2()

        """Restaurant Name Page"""

        with allure.step("Enter restaurant name"):
            restaurant_name = RestaurantNamePage()
            restaurant_name.fill_restaurant_name()

        with allure.step("Select 'Start' button of 'Restaurant Name' page"):
            restaurant_name.click_start_btn()

        """Commercial License"""

        with allure.step("Select 'Start' button of Commercial Activities"):
            commercial_license = CommercialLicensePage()
            commercial_license.click_activities_start_btn()

        """Service Activities Page"""

        with allure.step("Select 'Bakery' button on 'Service List' page"):
            service_list = CommercialLicenseServiceListPage()
            service_list.click_bakery_btn()

        with allure.step("Select 'Next' button on 'Service List' page"):
            service_list.click_next_btn()

        """Provide Meal Page"""

        with allure.step("Select 'Yes' button on 'Provide Meal' page"):
            provide_meal = CommercialLicenseProvideMealPage()
            provide_meal.click_yes_btn()

        with allure.step("Select 'Next' button on 'Provide Meal' page"):
            provide_meal.click_next_btn()

        """Delivery Meal Page"""

        with allure.step("Select 'Yes' button on 'Delivery Food' page"):
            delivery_food = CommercialLicenseDeliveryFoodPage()
            delivery_food.click_yes_btn()

        with allure.step("Select 'Next' button on 'Provide Meal' page"):
            delivery_food.click_next_btn()

        """Activities Summary Page"""

        with allure.step("Select 'Legal Form' button"):
            summary_of_activities = SummaryOfActivitiesPage()
            summary_of_activities.click_legal_form_btn()

        """Legal Form - Non Emirati - Sole - Establishment"""

        """Sole and Partnership Page"""

        with allure.step("Select 'Sole' button"):
            sole_partnership_page = CommercialLicenseSoleOrPartnershipPage()
            sole_partnership_page.click_sole_btn()

        with allure.step("Select 'Next' button"):
            sole_partnership_page.click_next_btn()

        """Establishment Page"""

        with allure.step("Select 'Establishment' button in 'Establishment' page"):
            establishment = CommercialLicenseEstablishmentPage()
            establishment.click_establishment_btn()

        with allure.step("Select 'Next' button in 'Establishment' page"):
            establishment.click_next_btn()

        """Summary screen of Leagal form"""

        with allure.step("Select 'Trade Name' button in 'Legal Form' page"):
            legal_form_summary = SummaryOfLegalFormPage()
            legal_form_summary.click_select_trade_name()

        """Trade name Page"""

        with allure.step("Select 'Start' button of 'Select your trade name' step"):
            trade_name = TradeNamePage()
            trade_name.click_select_trade_name_start()

        """Enter Trade Name Page"""

        # with allure.step("Enter 'Trade Name' in English"):
        #     enter_trade_name = EnterTradeNamePage()
        #     enter_trade_name.fill_trade_name_english()

        with allure.step("Enter 'Trade Name' in Arabic"):
            enter_trade_name = EnterTradeNamePage()
            enter_trade_name.fill_trade_name_arabic()

        with allure.step("Select 'Month' from the drop down"):
            enter_trade_name.select_reservation_months("12 months")

        with allure.step("Select 'Submit For Approval' button of Enter Trade Name Page"):
            enter_trade_name.click_submit_for_approval_btn()

        """Trade Name Approval Page"""

        with allure.step("Enter 'Trade Name' in Arabic"):

            approval = TradeNameApprovalPage()
            approval.click_next_btn()
