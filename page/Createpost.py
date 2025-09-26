import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("project root path--",project_root)
media_folder = os.path.join(project_root, "media")
image_file = os.path.join(media_folder, "sample_image.jpg")
video_file = os.path.join(media_folder, "sample_video.mp4.mp4")

screenshots_folder = os.path.join(project_root, "screenshots")
os.makedirs(screenshots_folder, exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://emilo-live-stream-front.vercel.app/login")

try:

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))
    ).send_keys(EMAIL)

    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder=\"What's on your mind?\"]"))
    )
    print("Login successful!")

except TimeoutException:
    print("Login failed or element not found!")
    screenshot_path = os.path.join(screenshots_folder, "login_failed.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
    driver.quit()
    exit()


def create_post(text=None, media_path=None):
    try:
        post_input = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder=\"What's on your mind?\"]")
        post_input.clear()
        if text:
            post_input.send_keys(text)

        if media_path:

            driver.find_element(By.CSS_SELECTOR, "button.flex.items-center.gap-2.text-sm.px-4.py-2.rounded-lg.bg-purple-50").click()
            # Directly use input[type='file'] for upload
            file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            print("file input---",file_input,media_path)
            file_input.send_keys(media_path)


        driver.find_element(By.CSS_SELECTOR, "button.bg-gradient-to-r.from-blue-500.via-purple-500.to-red-500.text-white").click()


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '{}')]".format(text))) if text else EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
        print(f"Post created: {text or media_path}")

    except Exception as e:
        print(f"Failed to create post: {e}")
        screenshot_path = os.path.join(screenshots_folder, f"post_failed.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")


create_post(text="Hello, this is a text post!")
create_post(media_path=image_file)
create_post(media_path=video_file)


driver.quit()
print("All posts done!")
