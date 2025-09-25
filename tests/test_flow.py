# tests/test_flow.py

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# ------------------ Fixture to initialize and quit driver ------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ------------------ Test 1: Register User ------------------
def test_a_register_user(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/register")
    # Fill in registration form (replace selectors)
    # Example:
    # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("newuser@example.com")
    # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("Password123")
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Verify registration success (replace with actual selector/assertion)
    assert True  # Replace with real assertion

# ------------------ Test 2: Create Post ------------------
def test_b_create_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/create")
    # Fill in post creation form (replace selectors)
    # Example:
    # driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Write something']").send_keys("My first post")
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Verify post creation
    assert True  # Replace with real assertion

# ------------------ Test 3: View Post ------------------
def test_c_view_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/view")
    # Interact with/view a post (replace selectors)
    # Example:
    # post = driver.find_element(By.CSS_SELECTOR, "div.post:first-child")
    # assert post is not None
    assert True  # Replace with real assertion

# ------------------ Test 4: Comment on a Post ------------------
def test_d_comment_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/")
    # Add your comment test code (replace selectors)
    # comment_box = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Add a comment']")
    # comment_box.send_keys("Nice post!")
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert True  # Replace with real assertion

# ------------------ Test 5: Like a Post ------------------
def test_e_like_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/")
    # Add your like test code (replace selectors)
    # like_button = driver.find_element(By.CSS_SELECTOR, "...your selector...")
    # like_button.click()
    assert True  # Replace with real assertion

# ------------------ Test 6: Login (run last) ------------------
def test_z_login_flow(driver):
    login = LoginPage(driver)

    # Step 1: Open login page
    login.open()

    # Step 2: Perform login
    login.login(EMAIL, PASSWORD)

    # Step 3: Verify login success by checking post box
    post_box = driver.find_elements(By.CSS_SELECTOR, "textarea[placeholder=\"What's on your mind?\"]")
    assert post_box, "Login failed: post box not found"
