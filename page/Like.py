from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.get("https://emilo-live-stream-front.vercel.app/login")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

like_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > section:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)")
like_button.click()

print("Post liked!")

driver.quit()
