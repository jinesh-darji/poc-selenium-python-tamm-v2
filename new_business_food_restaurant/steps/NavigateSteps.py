import allure

from new_business_food_restaurant.pages.LandingPage.HomeGrantPage import HomeGrantPage
from new_business_food_restaurant.pages.LandingPage.HomePage import HomePage
from new_business_food_restaurant.pages.Login.LoginTAMMPage import LoginTAMMPage
from new_business_food_restaurant.pages.Login.TAMMSmartPassPage import TAMMSmartPassPage
from new_business_food_restaurant.pages.LandingPage.RetaurantName import RestaurantNamePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicensePage import CommercialLicensePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseServiceListPage import \
    CommercialLicenseServiceListPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseProvideMealPage import \
    CommercialLicenseProvideMealPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseDeliveryFoodPage import \
    CommercialLicenseDeliveryFoodPage
from new_business_food_restaurant.pages.CommercialLicense.SummaryOfActivitiesPage import SummaryOfActivitiesPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseSoleOrPartnershipPage import \
    CommercialLicenseSoleOrPartnershipPage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseEstablishmentPage import \
    CommercialLicenseEstablishmentPage
from new_business_food_restaurant.pages.CommercialLicense.SummaryOfLegalFormPage import SummaryOfLegalFormPage
from new_business_food_restaurant.pages.CommercialLicense.TradeNamepage import TradeNamePage
from new_business_food_restaurant.pages.CommercialLicense.EnterTradeName import EnterTradeNamePage
from new_business_food_restaurant.pages.CommercialLicense.TradeNameApprovalPage import TradeNameApprovalPage
from new_business_food_restaurant.pages.CommercialLicense.TradeNamePaymentSuccessPage import TradeNamePaymentSuccessPage
from new_business_food_restaurant.pages.CommercialLicense.TradeNameSuccessPage import TradeNameSuccessPage
from new_business_food_restaurant.pages.CommercialLicense.NoDocumentRequired import NoDocumentRequiredPage
from new_business_food_restaurant.pages.CommercialLicense.SummaryOfCommercialLicensePage import \
    SummaryOfCommercialLicensePage
from new_business_food_restaurant.pages.CommercialLicense.CommercialLicenseIssuedPage import CommercialLicenseIssuedPage


class NavigateSteps:

    """Home Grant Page"""

    @staticmethod
    def go_to_start_new_restaurant_page():
        with allure.step("Select 'Start a New Restaurant' Button on 'Home Grant' page"):
            home_grant_page = HomeGrantPage()
            home_grant_page.click_start_a_new_restaurant_btn()

    @staticmethod
    def go_to_manage_application_page():
        with allure.step("Select 'Manage Application' Button on 'Home Grant' page"):
            home_grant_page = HomeGrantPage()
            home_grant_page.click_manage_application_btn()

    @staticmethod
    def go_to_market_report_page():
        with allure.step("Select 'Market Report' Button on 'Home Grant' page"):
            home_grant_page = HomeGrantPage()
            home_grant_page.click_market_reports_btn()

    # """With TAMM Portal Login with persona 1"""
    #
    # @staticmethod
    # def go_to_login_with_user1():
    #
    #     """Login Page"""
    #
    #     with allure.step("Select 'Login with SmartPass' button and navigate to TAMM smartpass portal"):
    #         login = LoginTAMMPage()
    #         login.click_login_with_smartpass_btn()
    #
    #     """TAMM Login Page"""
    #
    #     with allure.step("Enter 'Username' in text field"):
    #         tammlogin = TAMMSmartPassPage()
    #         tammlogin.fill_username1()
    #
    #     with allure.step("Enter 'password' in text field"):
    #         tammlogin.fill_password1()
    #
    #     with allure.step("Select 'Login' button and navigate to TAMM Application"):
    #         tammlogin.click_login_button()

    """Without TAMM Portal Login with persona 1"""

    @staticmethod
    def go_to_login_with_user1():
        with allure.step("Select Persona 1"):
            login = LoginTAMMPage()
            login.click_non_emirati_user_one_btn()

    # """With TAMM Portal Login with persona 2"""
    #
    # @staticmethod
    # def go_to_login_with_user2():
    #
    #     """Login Page"""
    #
    #     with allure.step("Select 'Login with SmartPass' button and navigate to TAMM smartpass portal"):
    #         login = LoginTAMMPage()
    #         login.click_login_with_smartpass_btn()
    #
    #     """TAMM Login Page"""
    #
    #     with allure.step("Enter 'Username' in text field"):
    #         tammlogin = TAMMSmartPassPage()
    #         tammlogin.fill_username2()
    #
    #     with allure.step("Enter 'password' in text field"):
    #         tammlogin.fill_password2()
    #
    #     with allure.step("Select 'Login' button and navigate to TAMM Application"):
    #         tammlogin.click_login_button()

    """Without TAMM Portal Login with persona 2"""

    @staticmethod
    def go_to_login_with_user2():
        with allure.step("Select Persona 2"):
            login = LoginTAMMPage()
            login.click_emirati_user_two_btn()

    # """With TAMM Portal Login with persona 3"""
    #
    # @staticmethod
    # def go_to_login_with_user3():
    #
    #     """Login Page"""
    #
    #     with allure.step("Select 'Login with SmartPass' button and navigate to TAMM smartpass portal"):
    #         login = LoginTAMMPage()
    #         login.click_login_with_smartpass_btn()
    #
    #     """TAMM Login Page"""
    #
    #     with allure.step("Enter 'Username' in text field"):
    #         tammlogin = TAMMSmartPassPage()
    #         tammlogin.fill_username3()
    #
    #     with allure.step("Enter 'password' in text field"):
    #         tammlogin.fill_password3()
    #
    #     with allure.step("Select 'Login' button and navigate to TAMM Application"):
    #         tammlogin.click_login_button()

    """Without TAMM Portal Login with persona 3"""

    @staticmethod
    def go_to_login_with_user3():
        with allure.step("Select Persona 3"):
            login = LoginTAMMPage()
            login.click_emirati_user_three_btn()

    # """With TAMM Portal Login with persona 4"""
    #
    # @staticmethod
    # def go_to_login_with_user4():
    #
    #     """Login Page"""
    #
    #     with allure.step("Select 'Login with SmartPass' button and navigate to TAMM smartpass portal"):
    #         login = LoginTAMMPage()
    #         login.click_login_with_smartpass_btn()
    #
    #     """TAMM Login Page"""
    #
    #     with allure.step("Enter 'Username' in text field"):
    #         tammlogin = TAMMSmartPassPage()
    #         tammlogin.fill_username4()
    #
    #     with allure.step("Enter 'password' in text field"):
    #         tammlogin.fill_password4()
    #
    #     with allure.step("Select 'Login' button and navigate to TAMM Application"):
    #         tammlogin.click_login_button()

    """Without TAMM Portal Login with persona 4"""

    @staticmethod
    def go_to_login_with_user4():
        with allure.step("Select Persona 4"):
            login = LoginTAMMPage()
            login.click_non_emirati_user_four_btn()

    # """With TAMM Portal Login with persona 5"""
    #
    # @staticmethod
    # def go_to_login_with_user5():
    #
    #     """Login Page"""
    #
    #     with allure.step("Select 'Login with SmartPass' button and navigate to TAMM smartpass portal"):
    #         login = LoginTAMMPage()
    #         login.click_login_with_smartpass_btn()
    #
    #     """TAMM Login Page"""
    #
    #     with allure.step("Enter 'Username' in text field"):
    #         tammlogin = TAMMSmartPassPage()
    #         tammlogin.fill_username5()
    #
    #     with allure.step("Enter 'password' in text field"):
    #         tammlogin.fill_password5()
    #
    #     with allure.step("Select 'Login' button and navigate to TAMM Application"):
    #         tammlogin.click_login_button()

    """Without TAMM Portal Login with persona 5"""

    @staticmethod
    def go_to_login_with_user5():
        with allure.step("Select Persona 5"):
            login = LoginTAMMPage()
            login.click_non_emirati_user_five_btn()

    """Issued Commercial License with rent"""

    @staticmethod
    def go_to_commercial_license_issued_page():

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
            sole_partner_page = CommercialLicenseSoleOrPartnershipPage()
            sole_partner_page.click_sole_btn()

        with allure.step("Select 'Next' button"):
            sole_partner_page.click_next_btn()

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

        """Trade Name Process"""

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

        """Payment Success Page"""

        with allure.step("Open payment tab"):
            trade_name.click_payment_open_tab()

        with allure.step("Select 'Payment' button"):
            trade_name.click_payment_start()

        """Payment Success Page"""

        with allure.step("Verify Success Message"):
            payment_page = TradeNamePaymentSuccessPage()
            payment_page.is_success_text_present()

        with allure.step("Click on 'Commercial License' link"):
            payment_page.click_commercial_license_link()

        """Commercial License Page"""

        with allure.step("Open Trade Name Tab"):
            commercial_license.click_btn_trade_name_tab()

        with allure.step("CLick on 'View Details' page"):
            commercial_license.click_btn_view_details_trade_name()

        """Trade name Page"""

        with allure.step("Select Intial Approval Tab"):
            trade_name.click_initial_approval_tab()

        with allure.step("Select 'Issued' button"):
            trade_name.click_btn_issued_commercial_license()

        """Trade Name Success Page"""

        with allure.step("Select 'Download' button"):
            trade_name_success = TradeNameSuccessPage()
            trade_name_success.click_download_btn()

        with allure.step("Select 'Document' button"):
            trade_name_success.click_documents_btn()

        """Document Process"""

        """Download Success Page"""

        with allure.step("No Document text is displayed"):
            summary_document = NoDocumentRequiredPage()
            summary_document.is_no_document_required_display()

        with allure.step("Select 'Issue Commercial License' button"):
            summary_document.click_issue_commercial_license_btn()

        """Commercial License Process"""

        with allure.step("Select 'Yes' radio button"):
            summary_commercial_licaense = SummaryOfCommercialLicensePage()
            summary_commercial_licaense.click_rent_yes_radio()

        with allure.step("Fill 'Tawtheeq Number' in text field"):
            summary_commercial_licaense.fill_tawtheeq_number()

        with allure.step("Select 'Submit' button"):
            summary_commercial_licaense.click_submit_your_application()

        """Commercial License Success Page"""

        with allure.step("Select 'Download Certificate' button"):
            issued = CommercialLicenseIssuedPage()
            issued.click_download_certificate_btn()

        with allure.step("Select 'Schedule ADFCA Inspection' button"):
            issued = CommercialLicenseIssuedPage()
            issued.click_schedule_adfca_inspection_btn()

    """Issued Commercial License without rent"""

    @staticmethod
    def go_to_commercial_license_issued_without_rent_page():
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

        """Trade Name Process"""

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

        """Payment Success Page"""

        with allure.step("Open payment tab"):
            trade_name.click_payment_open_tab()

        with allure.step("Select 'Payment' button"):
            trade_name.click_payment_start()

        """Payment Success Page"""

        with allure.step("Verify Success Message"):
            payment_page = TradeNamePaymentSuccessPage()
            payment_page.is_success_text_present()

        with allure.step("Click on 'Commercial License' link"):
            payment_page.click_commercial_license_link()

        """Commercial License Page"""

        with allure.step("Open Trade Name Tab"):
            commercial_license.click_btn_trade_name_tab()

        with allure.step("CLick on 'View Details' page"):
            commercial_license.click_btn_view_details_trade_name()

        """Trade name Page"""

        with allure.step("Select Intial Approval Tab"):
            trade_name.click_initial_approval_tab()

        with allure.step("Select 'Issued' button"):
            trade_name.click_btn_issued_commercial_license()

        """Trade Name Success Page"""

        with allure.step("Select 'Download' button"):
            tradenamesuccess = TradeNameSuccessPage()
            tradenamesuccess.click_download_btn()

        with allure.step("Select 'Document' button"):
            trade_name_success = TradeNameSuccessPage()
            trade_name_success.click_documents_btn()

        """Document Process"""

        """Download Success Page"""

        with allure.step("No Document text is displayed"):
            summary_document = NoDocumentRequiredPage()
            summary_document.is_no_document_required_display()

        with allure.step("Select 'Issue Commercial License' button"):
            summary_document.click_issue_commercial_license_btn()

        """Commercial License Process"""

        with allure.step("Select 'No' radio button"):
            summary_commercial_license = SummaryOfCommercialLicensePage()
            summary_commercial_license.click_rent_no_radio()

        with allure.step("Select 'Submit' button"):
            summary_commercial_license.click_submit_your_application()

        """Commercial License Success Page"""

        with allure.step("Select 'Download Certificate' button"):
            issued = CommercialLicenseIssuedPage()
            issued.click_download_certificate_btn()

        with allure.step("Select 'Rent' button"):
            issued.click_rent_btn()

