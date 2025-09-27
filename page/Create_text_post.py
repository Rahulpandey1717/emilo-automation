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


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://emilo-task.vercel.app/login")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("✅ Login successful!")


post_textarea = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder=\"What's on your mind?\"]"))
)
post_textarea.clear()
post_text = "Hello, this is a test text post!"
post_textarea.send_keys(post_text)
time.sleep(1)


post_button = driver.find_element(
    By.CSS_SELECTOR,
    "button[class=' bg-gradient-to-r from-blue-500 via-purple-500 to-red-500 text-white text-sm font-medium px-6 py-2 rounded-lg shadow hover:brightness-110 transition-all']"
)
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_button)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", post_button)


time.sleep(3)
screenshot_path = os.path.join(screenshots_folder, "text_post_failed.png")
driver.save_screenshot(screenshot_path)
print("❌ Text post failed!")

time.sleep(5)
driver.quit()
