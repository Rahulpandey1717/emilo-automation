import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenshots_folder = os.path.join(project_root, "screenshots")
os.makedirs(screenshots_folder, exist_ok=True)
screenshot_path = os.path.join(screenshots_folder, "comment_failed.png")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://emilo-task.vercel.app/")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("✅ Login successful!")

time.sleep(5)

comment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,
         "body > div:nth-child(1) main section:nth-child(2) section:nth-child(1) div:nth-child(2) div:nth-child(4) > button:nth-child(2)")
    )
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", comment_button)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", comment_button)
time.sleep(1)

comment_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Write a comment...']"))
)
comment_input.send_keys("Hello! This is a test comment.")

send_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='bg-purple-500 text-white px-4 py-2 rounded-xl hover:bg-purple-600 transition-colors text-sm']"))
)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", send_button)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", send_button)

time.sleep(10)
print("✅ Comment sent (check server response).")

driver.save_screenshot(screenshot_path)
print(f"📸 Screenshot saved at {screenshot_path}")

driver.quit()
