import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
video_file = os.path.join(project_root, "media", "4114797-uhd_3840_2160_25fps.mp4")
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

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder=\"What's on your mind?\"]"))
)

driver.find_element(By.CSS_SELECTOR, "button.flex.items-center.gap-2.text-sm.px-4.py-2.rounded-lg.bg-purple-50").click()
time.sleep(1)

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(video_file)
print(f"📂 Uploading video: {video_file}")

time.sleep(1)
pyautogui.press('esc')

driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
time.sleep(1)

post_button = driver.find_element(
    By.CSS_SELECTOR,
    "button[class=' bg-gradient-to-r from-blue-500 via-purple-500 to-red-500 text-white text-sm font-medium px-6 py-2 rounded-lg shadow hover:brightness-110 transition-all']"
)
driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", post_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", post_button)

time.sleep(7)
screenshot_path = os.path.join(screenshots_folder, "video_post_failed.png")
driver.save_screenshot(screenshot_path)
print("❌ Video post failed. Screenshot saved.")

time.sleep(5)
driver.quit()
