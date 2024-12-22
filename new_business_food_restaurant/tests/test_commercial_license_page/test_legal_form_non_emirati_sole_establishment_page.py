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
from new_business_food_restaurant.pages.CommercialLicense.OwnershipDetailsPage import OwnershipDetailsPage
from new_business_food_restaurant.pages.CommercialLicense.AddSponsorForm import AddSponsorForm


class TestLegalFormNonEmiratiSoleEstablishmentPage:

    @pytest.mark.smoke
    def test_legal_form_non_emirati_sole_establishment_page(self):

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

        NavigateSteps.go_to_login_with_user1()

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

        """Ownership Page"""

        with allure.step("Select 'Add Sponsor' button in 'Ownership' page"):
            add_sponsor = OwnershipDetailsPage()
            add_sponsor.click_add_sponsor_btn()

        """Add Sponsor Details"""

        with allure.step("Add 'English Name' in 'Sponsor' Details"):
            sponsor_form = AddSponsorForm()
            sponsor_form.fill_name_in_english()

        with allure.step("Add 'Arabic Name' in 'Sponsor' Details"):
            sponsor_form.fill_name_in_arabic()

        with allure.step("Add 'DOB' in 'Sponsor' Details"):
            sponsor_form.set_dob_date()

        with allure.step("Add 'Emirati ID' in 'Sponsor' Details"):
            sponsor_form.fill_emirati_id()

        with allure.step("Add 'Email' in 'Sponsor' Details"):
            sponsor_form.fill_email()

        with allure.step("Add 'Phone Number' in 'Sponsor' Details"):
            sponsor_form.fill_phone_number()

        with allure.step("Add 'Emirati' in 'Sponsor' Details"):
            sponsor_form.fill_emirates()

        with allure.step("Add 'City' in 'Sponsor' Details"):
            sponsor_form.fill_city()

        with allure.step("Add 'Area' in 'Sponsor' Details"):
            sponsor_form.fill_area()

        with allure.step("Add 'Street' in 'Sponsor' Details"):
            sponsor_form.fill_street()

        with allure.step("Add 'Building' in 'Sponsor' Details"):
            sponsor_form.fill_building()

        with allure.step("Select 'Submit' in 'Sponsor' Details"):
            sponsor_form.click_submit_btn()

        """Ownership Page"""

        with allure.step("Select 'Next' button"):
            add_sponsor = OwnershipDetailsPage()
            add_sponsor.click_next_btn()
