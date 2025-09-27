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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://emilo-task.vercel.app/")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("✅ Login successful!")

time.sleep(5)

post_container = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > section:nth-child(2) > section:nth-child(1) > div:nth-child(2)")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_container
)
time.sleep(1)

like_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,
         "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > section:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", like_button
)
time.sleep(1)
like_button.click()

print("✅ Post liked successfully!")
time.sleep(5)
driver.quit()
