import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------- Test Data -----------------
FULL_NAME = "Rahul Test"
PASSWORD = "Test@123"
COMMENT_TEXT = "Automated comment on latest post!"
MEDIA_FOLDER = r"C:\Users\Rahul\PycharmProjects\emilo-socialmedia-selenium\media"
IMAGE_FILE = os.path.join(MEDIA_FOLDER, "test_image.jpg")
VIDEO_FILE = os.path.join(MEDIA_FOLDER, "test_video.mp4")

# ----------------- Helper Functions -----------------
def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"rahul.test{timestamp}@example.com"

def wait_and_click(driver, css_selector, timeout=15):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )
    element.click()
    time.sleep(2)

def wait_and_send_keys(driver, css_selector, text, timeout=15):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    element.send_keys(text)
    time.sleep(1)

# ----------------- Register & Login -----------------
def register(driver, email):
    driver.get("https://emilo-live-stream-front.vercel.app/register")
    wait_and_send_keys(driver, "input[placeholder='Full Name']", FULL_NAME)
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_send_keys(driver, "input[placeholder='Confirm Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    print(f"Registration completed with email: {email}")
    time.sleep(5)

def login(driver, email):
    driver.get("https://emilo-live-stream-front.vercel.app/login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    print(f"Login completed with email: {email}")
    time.sleep(5)

# ----------------- Create Post -----------------
def create_post(driver, text=None, image_path=None, video_path=None):
    post_input_css = "textarea[placeholder=\"What's on your mind?\"]"
    post_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, post_input_css))
    )
    if text:
        post_input.send_keys("\n" + text)

    # Upload image or video
    if image_path or video_path:
        wait_and_click(driver, "button[class='flex items-center gap-2 text-sm px-4 py-2 rounded-lg bg-purple-50 dark:bg-gray-700 text-purple-600 dark:text-purple-400 hover:bg-purple-100 dark:hover:bg-gray-600 transition']")
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        if image_path and os.path.exists(image_path):
            file_input.send_keys(image_path)
            print("Image selected.")
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='test_image']"))
            )
        if video_path and os.path.exists(video_path):
            file_input.send_keys(video_path)
            print("Video selected.")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
            )

    # Click Post button
    wait_and_click(driver, "button.bg-gradient-to-r.from-blue-500.via-purple-500.to-red-500.text-white")
    print(f"Post created: {text or image_path or video_path}")
    time.sleep(3)

# ----------------- Like & Comment Latest Post -----------------
def like_and_comment_latest_post(driver, comment_text=COMMENT_TEXT):
    time.sleep(3)
    posts = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.flex.flex-col.rounded-xl.bg-white"))
    )
    latest_post = posts[0]  # newest post
    driver.execute_script("arguments[0].scrollIntoView(true);", latest_post)
    time.sleep(2)

    # Like
    like_button = latest_post.find_element(By.CSS_SELECTOR, "button[aria-label='Like']")
    like_button.click()
    print("Liked the latest post.")
    time.sleep(2)

    # Comment
    comment_box = latest_post.find_element(By.CSS_SELECTOR, "textarea[placeholder='Write a comment...']")
    comment_box.send_keys(comment_text)
    send_button = latest_post.find_element(By.CSS_SELECTOR, "button[type='submit']")
    send_button.click()
    print("Commented on the latest post.")
    time.sleep(2)

# ----------------- Pytest Test -----------------
def test_full_social_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        email = generate_unique_email()

        # Register
        register(driver, email)
        driver.quit()

        # Login
        driver = webdriver.Chrome()
        driver.maximize_window()
        login(driver, email)

        # Create posts
        create_post(driver, text="Hello, this is a text post!")
        create_post(driver, image_path=IMAGE_FILE)
        create_post(driver, video_path=VIDEO_FILE)

        # Like & Comment latest post
        like_and_comment_latest_post(driver, comment_text="This is awesome!")

    finally:
        time.sleep(3)
        driver.quit()
        print("All actions completed successfully.")
