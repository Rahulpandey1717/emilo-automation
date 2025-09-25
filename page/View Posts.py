from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://emilo-live-stream-front.vercel.app/login")

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

post_img = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > section:nth-child(2) > section:nth-child(1) > div:nth-child(2) > img:nth-child(3)"))
)


post_container = post_img.find_element(By.XPATH, "..")  # parent div of the image
post_text = post_container.text

print("Post Text:", post_text)
print("Post Image URL:", post_img.get_attribute("src"))

driver.quit()
