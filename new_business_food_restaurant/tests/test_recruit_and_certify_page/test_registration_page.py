import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.RecruitAndCertify.RegistrationPage import RegistrationPage
from new_business_food_restaurant.pages.RecruitAndCertify.RecruitAndCertifyPage import RecruitAndCertifyPage
from new_business_food_restaurant.pages.RecruitAndCertify.EstablishmentCardPage import EstablishmentCardPage
from new_business_food_restaurant.pages.RecruitAndCertify.ElectronicSignatureCardPage import ElectronicSignatureCardPage
from new_business_food_restaurant.pages.RecruitAndCertify.MOHREEstablishmentCardPage import MOHREEstablishmentCardPage
from new_business_food_restaurant.pages.RecruitAndCertify.ApplyForQuotaPage import ApplyforQuotaPage


class TestRegistrationPage:

    @pytest.mark.smoke
    def test_registration_page(self):

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

        with allure.step("Select 'start' button of recruitment"):
            home.click_recruit_and_certify_start_btn()

        """Recruit & Certify Page"""

        with allure.step("Select 'Registration' button"):
            recruit_certify = RecruitAndCertifyPage()
            recruit_certify.click_registration_btn()

        """Registration Page"""

        with allure.step("Select 'Establishment card' button"):
            registration = RegistrationPage()
            registration.click_establishment_card_btn()

        """Registration Sub Pages"""

        with allure.step("Establishment Card text is displayed"):
            establishment_card = EstablishmentCardPage()
            assert_that(establishment_card.is_establishment_card_text_is_present(),
                        "Establishment Card text is not displayed")

        with allure.step("Select 'E-Signature Card' link"):
            establishment_card.click_esignature_card_link()

        with allure.step("Electronic Signature Card text is displayed"):
            esignature = ElectronicSignatureCardPage()
            assert_that(esignature.is_electronic_signature_card_text_is_present(),
                        "Electronic Signature Card text is displayed")

        with allure.step("Select 'MOHRE establishment card' link"):
            establishment_card.click_mohre_establishment_card_link()

        with allure.step("MOHRE establishment card text is displayed"):
            mohre = MOHREEstablishmentCardPage()
            assert_that(mohre.is_mohre_establishment_card_text_is_present(),
                        "MOHRE establishment card text is not displayed")

        with allure.step("Select 'Visa quota approval' link"):
            establishment_card.click_visa_quota_approval_link()

        with allure.step("Apply for Quota text is display"):
            visa_quota = ApplyforQuotaPage()
            assert_that(visa_quota.is_visa_quota_approval_text_is_present(), "Apply for Quota text is not display")










