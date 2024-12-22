import pytest
import allure
from hamcrest import assert_that

from new_business_food_restaurant.pages.LandingPage.LandingGuidelinePage import LandingGuidePage
from new_business_food_restaurant.steps.NavigateSteps import NavigateSteps
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.DesignAndADFCAInspection.ADFCAInspectionPage import ADFCAInspectionPage
from new_business_food_restaurant.pages.RecruitAndCertify.RecruitAndCertifyPage import RecruitAndCertifyPage
from new_business_food_restaurant.pages.RecruitAndCertify.RecruitmentPage import RecruitmentPage
from new_business_food_restaurant.pages.RecruitAndCertify.WorkOfferPage import WorkOfferPage
from new_business_food_restaurant.pages.RecruitAndCertify.WorkPermitPage import WorkPermitPage
from new_business_food_restaurant.pages.RecruitAndCertify.EntryPermitPage import EntryPermitPage
from new_business_food_restaurant.pages.RecruitAndCertify.ConductMedicalTestPage import ConductMedicalTestPage
from new_business_food_restaurant.pages.RecruitAndCertify.WorkContractPage import WorkContractPage
from new_business_food_restaurant.pages.RecruitAndCertify.MedicalInsurancePage import MedicalInsurancePage
from new_business_food_restaurant.pages.RecruitAndCertify.EmiratesIDPage import EmiratesIDPage
from new_business_food_restaurant.pages.RecruitAndCertify.ResidenceVisaPage import ResidenceVisaPage


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
            recruit_certify.click_recruitment_btn()

        """Recruitment Page"""

        with allure.step("Select 'Recruitment card' button"):
            recruitment = RecruitmentPage()
            recruitment.click_work_offer_btn()

        """Recruitment Sub Pages"""

        with allure.step("Work offer text is displayed"):
            work_offer = WorkOfferPage()
            assert_that(work_offer.is_work_offer_text_is_present(), "Work offer text is not displayed")

        with allure.step("Click on 'Work Permit' link"):
            work_offer.click_work_permit_side_menu_link()

        with allure.step("Work Permit text is displayed"):
            work_permit = WorkPermitPage()
            assert_that(work_permit.is_work_permit_text_is_present(), "Work Permit text is not displayed")

        with allure.step("Click on 'Entry Permit' link"):
            work_offer.click_entry_permit_side_menu_link()

        with allure.step("Entry Permit text is displayed"):
            entry_permit = EntryPermitPage()
            assert_that(entry_permit.is_entry_permit_text_is_present(), "Entry Permit text is not displayed")

        with allure.step("Click on 'Conduct Medical Test' link"):
            work_offer.click_medical_test_side_menu_link()

        with allure.step("Conduct Medical Test text is displayed"):
            medical_test = ConductMedicalTestPage()
            assert_that(medical_test.is_conduct_medical_test_text_is_present(),
                        "Conduct Medical Test text is not displayed")

        with allure.step("Click on 'Work Contract' link"):
            work_offer.click_work_contract_side_menu_link()

        with allure.step("Work Contract text is displayed"):
            work_contract = WorkContractPage()
            assert_that(work_contract.is_work_contract_text_is_present(),
                        "Work Contract text is not displayed")

        with allure.step("Click on 'Medical Insurance' link"):
            work_offer.click_medical_insurance_side_menu_link()

        with allure.step("Medical Insurance text is displayed"):
            medical_insurance = MedicalInsurancePage()
            assert_that(medical_insurance.is_medical_insurance_text_is_present(),
                        "Medical Insurance text is not displayed")

        with allure.step("Click on 'Emirates ID' link"):
            work_offer.click_emirates_id_side_menu_link()

        with allure.step("Emirates ID text is displayed"):
            emirates_id = EmiratesIDPage()
            assert_that(emirates_id.is_emirates_id_text_is_present(), "Emirates ID text is not displayed")

        with allure.step("Click on 'Residence Visa' link"):
            work_offer.click_residence_visa_side_menu_link()

        with allure.step("Residence Visa text is displayed"):
            residence_visa = ResidenceVisaPage()
            assert_that(residence_visa.is_residence_visa_text_is_present(), "Residence Visa text is not displayed")






