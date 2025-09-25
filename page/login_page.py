# page/login_page.py

from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://emilo-live-stream-front.vercel.app/login"
        self.email_input = "input[placeholder='Email']"
        self.password_input = "input[placeholder='Password']"
        self.submit_button = "button[type='submit']"

    def open(self):
        """Open the login page"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)  # wait for page load

    def login(self, email, password):
        """Perform login with email and password"""
        self.driver.find_element(By.CSS_SELECTOR, self.email_input).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, self.password_input).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        time.sleep(5)  # wait for login to complete
