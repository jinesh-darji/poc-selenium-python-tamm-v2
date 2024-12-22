import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.MarketReportPage import MarketReportPage
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage


class TestMarketReportPage:

    @pytest.mark.smoke
    def test_market_report_page(self):
        """Landing Guide Page"""

        with allure.step("Select 'Start' button"):
            landing_guide = LandingGuidePage()
            landing_guide.click_start_btn()

        """Home Grant Page"""

        NavigateSteps.go_to_market_report_page()

        """Market Report Page"""

        with allure.step("Template one is displayed"):
            market_report = MarketReportPage()
            assert_that(market_report.is_template_one_is_displayed(), "Template one is not displayed")

        with allure.step("Click on Template One and Download it"):
            market_report.click_template_one()

        with allure.step("Template two is displayed"):
            assert_that(market_report.is_template_two_is_displayed(), "Template two is not displayed")

        with allure.step("Click on Template two and Download it"):
            market_report.click_template_two()

        with allure.step("Template three is displayed"):
            assert_that(market_report.is_template_three_is_displayed(), "Template three is not displayed")

        with allure.step("Click on Template three and Download it"):
            market_report.click_template_three()

        with allure.step("Template four is displayed"):
            assert_that(market_report.is_template_four_is_displayed(), "Template four is not displayed")

        with allure.step("Click on Template four and Download it"):
            market_report.click_template_four()

        with allure.step("Template five is displayed"):
            assert_that(market_report.is_template_five_is_displayed(), "Template five is not displayed")

        with allure.step("Click on Template five and Download it"):
            market_report.click_template_five()
