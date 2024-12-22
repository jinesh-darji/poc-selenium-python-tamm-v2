import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.Login.LoginTAMMPage import LoginTAMMPage
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

        with allure.step("is 'Khalifa Fund' text is displayed"):
            get_financing = GetFinancingPage()
            assert_that(get_financing.is_khalifa_fund_present(), "is 'Khalifa Fund' text is not displayed")







