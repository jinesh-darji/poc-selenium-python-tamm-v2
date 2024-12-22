import pytest
import allure
from hamcrest import assert_that

from framework.browser.Browser import Browser
from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ScheduleADFCAInspectionPage import ScheduleADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ArrangeAppoinmentPage import ArrangeAppointmentPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.DesignAndADFCAInspectionPage import DesignAndADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ScheduledADFCAInspectionPage import ScheduledADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.RejectedADFCAInspectionPage import RejectedADFCAInspectionPage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAPaymentPage import ADFCAPaymentPage


class TestADFCAInspectionWithRejectPage:

    @pytest.mark.smoke
    def test_adfca_inspection_with_reject_page(self):

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
            adfca_inspection.click_schedule_adfca_inspection()

        """Schedule ADFCA Inspection Page"""

        with allure.step("Select 'Submit Request' button"):
            schedule_adfca = ScheduleADFCAInspectionPage()
            schedule_adfca.click_submit_request_btn()

        """Appointment ADFCA Inspection Page"""

        with allure.step("Select 'Back Application' button"):
            arrange_adfca = ArrangeAppointmentPage()
            arrange_adfca.click_back_to_application_btn()

        """Application Page"""

        with allure.step("Select 'Start' button of Design and ADFCA Inspection"):
            home = HomePage()
            home.click_design_and_adfca_inspection_start_btn()

        """Design and ADFCA Inspection Page"""

        with allure.step("Select 'ADFCA Inspection' button"):
            design_and_adfca = DesignAndADFCAInspectionPage()
            design_and_adfca.click_adfca_inspection_btn()

        """Scheduled ADFCA Inspection Page"""

        with allure.step("Scheduled ADFCA inspection text is displayed"):
            scheduled_adfca = ScheduledADFCAInspectionPage()
            scheduled_adfca.is_adfca_inspection_scheduled_is_displayed()

        with allure.step("Refresh the page"):
            Browser.refresh_page()

        """ADFCA Rejection Page"""

        with allure.step("Verify ADFCA Rejection page"):
            reject_adfca = RejectedADFCAInspectionPage()
            reject_adfca.is_lbl_reject_description_is_present()

        with allure.step("Select 'Submit Request' button"):
            reject_adfca.click_submit_request_btn()

        """ADFCA Payment Page"""

        with allure.step("Fill card number in payment page"):
            payment = ADFCAPaymentPage()
            payment.fill_card_number()

        with allure.step("Select Expired Date"):
            payment.drpdwn_expired_date()

        with allure.step("Select 'Pay' button of ADFCA Payment Page"):
            payment.click_payment_btn()

        """ADFCA Inspection Satisfactory page"""

        with allure.step("Select 'Download' button"):
            arrange_adfca.click_download_btn()

        with allure.step("Select 'Back Application' button"):
            arrange_adfca.click_back_to_application_btn()




