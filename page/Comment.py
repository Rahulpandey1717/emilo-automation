from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://emilo-live-stream-front.vercel.app/login")

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)


driver.find_element(By.CSS_SELECTOR,
    "body > div:nth-child(1) main section:nth-child(2) section:nth-child(1) div:nth-child(2) div:nth-child(4) > button:nth-child(2)"
).click()

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Write a comment...']").send_keys("Hello! This is a test comment.")

driver.find_element(By.CSS_SELECTOR, "button[class*='text-white']").click()

print("Comment posted successfully!")
driver.quit()
