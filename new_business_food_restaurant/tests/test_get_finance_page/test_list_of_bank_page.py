import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.GetFinancing.BankListPage import BankListPage
from new_business_food_restaurant.pages.GetFinancing.GetFinancingPage import GetFinancingPage


class TestListOfBankPage:

    @pytest.mark.smoke
    def test_list_of_bank_page(self):

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

        NavigateSteps.go_to_commercial_license_issued_page()

        """ADFCA Inspection Page"""

        with allure.step("Select 'Schedule an Inspection with ADFCA' button"):
            adfca_inspection = ADFCAInspectionPage()
            adfca_inspection.click_application_link()

        """Home Page"""

        with allure.step("Select 'Start' button of Get Financing"):
            home.click_financing_start_btn()

        """Get Financing Page"""

        with allure.step("Select 'Find Out More' button of bank"):
            get_financing = GetFinancingPage()
            get_financing.click_find_out_more_bank_btn()

        """Bank List Page"""

        with allure.step("is list of bank is displayed"):
            bank_list = BankListPage()
            assert_that(bank_list.is_bank_list_is_present(), "is list of bank is not displayed")







