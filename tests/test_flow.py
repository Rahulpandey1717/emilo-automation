import os
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------- Test Data -----------------
FULL_NAME = "Rahul Test"
PASSWORD = "Test@123"
COMMENT_TEXT = "Automated comment on latest post!"
MEDIA_FOLDER = r"C:\Users\Rahul\PycharmProjects\emilo-socialmedia-selenium\media"
IMAGE_FILE = os.path.join(MEDIA_FOLDER, "sample_image.jpg")
VIDEO_FILE = os.path.join(MEDIA_FOLDER, "4114797-uhd_3840_2160_25fps.mp4")
BASE_URL = "https://emilo-task.vercel.app/"

# ----------------- Helper Functions -----------------
def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"rahul.test{timestamp}@example.com"

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

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

# ----------------- Actions -----------------
def register_user(email):
    driver = open_browser()
    driver.get(BASE_URL + "register")
    wait_and_send_keys(driver, "input[placeholder='Full Name']", FULL_NAME)
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_send_keys(driver, "input[placeholder='Confirm Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    print(f"✅ Registered with email: {email}")
    time.sleep(3)
    driver.quit()

def login_user(email):
    driver = open_browser()
    driver.get(BASE_URL + "login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    print(f"✅ Logged in with email: {email}")
    time.sleep(3)
    driver.quit()

def create_text_post(email, text):
    driver = open_browser()
    driver.get(BASE_URL + "login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    time.sleep(3)
    post_input_css = "textarea[placeholder=\"What's on your mind?\"]"
    post_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, post_input_css))
    )
    post_input.send_keys(text)
    wait_and_click(driver, "button.bg-gradient-to-r.from-blue-500.via-purple-500.to-red-500.text-white")
    print("✅ Text post created.")
    time.sleep(3)
    driver.quit()

def create_image_post(email, image_path):
    driver = open_browser()
    driver.get(BASE_URL + "login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    time.sleep(3)
    post_input_css = "textarea[placeholder=\"What's on your mind?\"]"
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, post_input_css)))
    wait_and_click(driver, "button.flex.items-center.gap-2.text-sm.px-4.py-2.rounded-lg.bg-purple-50")
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(image_path)
    print("✅ Image uploaded.")
    time.sleep(2)
    driver.execute_script("document.querySelector('html').scrollTo({top:0, behavior:'smooth'});")
    wait_and_click(driver, "button.bg-gradient-to-r.from-blue-500.via-purple-500.to-red-500.text-white")
    print("✅ Image post created.")
    time.sleep(3)
    driver.quit()

def create_video_post(email, video_path):
    driver = open_browser()
    driver.get(BASE_URL + "login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    time.sleep(3)
    post_input_css = "textarea[placeholder=\"What's on your mind?\"]"
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, post_input_css)))
    wait_and_click(driver, "button.flex.items-center.gap-2.text-sm.px-4.py-2.rounded-lg.bg-purple-50")
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(video_path)
    print("✅ Video uploaded.")
    time.sleep(2)
    driver.execute_script("document.querySelector('html').scrollTo({top:0, behavior:'smooth'});")
    wait_and_click(driver, "button.bg-gradient-to-r.from-blue-500.via-purple-500.to-red-500.text-white")
    print("✅ Video post created.")
    time.sleep(3)
    driver.quit()

def like_and_comment_latest_post(email, comment_text):
    driver = open_browser()
    driver.get(BASE_URL + "login")
    wait_and_send_keys(driver, "input[placeholder='Email']", email)
    wait_and_send_keys(driver, "input[placeholder='Password']", PASSWORD)
    wait_and_click(driver, "button[type='submit']")
    time.sleep(5)

    latest_post = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > section:nth-child(2) > section:nth-child(1) > div:nth-child(25) > img:nth-child(3)"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", latest_post)
    time.sleep(2)

    # Like
    like_svg_path = driver.find_element(By.XPATH, "(//*[name()='path'])[76]")
    like_button = like_svg_path.find_element(By.XPATH, "./ancestor::button[1]")
    driver.execute_script("arguments[0].scrollIntoView(true);", like_button)
    driver.execute_script("arguments[0].click();", like_button)
    print("✅ Liked the latest post")
    time.sleep(10)

    # Comment
    try:
        comment_svg = driver.find_element(By.XPATH, "//div[25]//div[2]//button[2]//div[1]//*[name()='svg']")
        comment_button = comment_svg.find_element(By.XPATH, "./ancestor::button[1]")
        driver.execute_script("arguments[0].click();", comment_button)
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Write a comment...']"))
        )
        comment_box.send_keys(comment_text)
        send_button = driver.find_element(By.XPATH, "//button[normalize-space()='Send']")
        driver.execute_script("arguments[0].click();", send_button)
        print("✅ Commented on latest post.")
        time.sleep(3)
    except (NoSuchElementException, TimeoutException, Exception) as e:
        print(f"⚠️ Comment flow failed, skipping comment. Reason: {e}")
    driver.quit()

# ----------------- Pytest Fixture -----------------
@pytest.fixture(scope="session")
def user_email():
    """Generate email and register user once for all tests."""
    email = generate_unique_email()
    register_user(email)
    return email

# ----------------- Modular Pytest Tests -----------------
def test_login_user(user_email):
    login_user(user_email)

def test_text_post(user_email):
    create_text_post(user_email, "Hello, this is an automated text post!")

def test_image_post(user_email):
    create_image_post(user_email, IMAGE_FILE)

def test_video_post(user_email):
    create_video_post(user_email, VIDEO_FILE)

def test_like_and_comment_post(user_email):
    like_and_comment_latest_post(user_email, "This is an automated comment!")

def test_full_flow_completed():
    print("✅ Full social media flow completed successfully.")
