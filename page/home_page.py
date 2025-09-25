from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def create_post(self, content):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create Post')]"))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, "content"))).send_keys(content)
        self.driver.find_element(By.XPATH, "//button[contains(., 'Submit')]").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{content}')]")))

    def comment_on_post(self, comment):
        self.wait.until(EC.presence_of_element_located((By.NAME, "comment"))).send_keys(comment)
        self.driver.find_element(By.XPATH, "//button[contains(., 'Comment')]").click()

    def like_post(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Like')]"))).click()

    def logout(self):
        try:
            self.driver.find_element(By.ID, "logout").click()
        except:
            self.driver.find_element(By.XPATH, "//a[contains(., 'Logout')]").click()
