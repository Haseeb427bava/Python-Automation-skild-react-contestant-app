"""it manages all the properties in the login page"""
from selenium.webdriver.common.by import By
from PageObject.RegistrationPage import RegistrationPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    """Elements of login_page"""
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[id='react-password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@id='login-submit']")
    SIGNUP_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Sign Up")
    INVALID_SIGNIN = (By.PARTIAL_LINK_TEXT, "invalid email")

    """the functions assert the signup text email, password and clicking on button"""
    """SignUp"""
    def signup_link_text(self):
        return self.driver.find_element(*LoginPage.SIGNUP_LINK_TEXT)

    """SignUp Click"""
    def click_signup_link_text(self):
        self.driver.find_element(*LoginPage.SIGNUP_LINK_TEXT).click()
        registrationpage = RegistrationPage(self.driver)
        return registrationpage
    """Email"""
    def give_email(self):
        return self.driver.find_element(*LoginPage.EMAIL_FIELD)
    """Password"""
    def give_password(self):
        return self.driver.find_element(*LoginPage.PASSWORD_FIELD)
    """Invalid msg"""
    def invalid_sms(self):
        invalid_text = (self.driver.find_element(*LoginPage.INVALID_SIGNIN)).text
        return invalid_text
    """Login-Button"""
    def click_signin_button(self):
        return self.driver.find_element(*LoginPage.SIGNIN_BUTTON)
