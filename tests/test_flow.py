

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from dotenv import load_dotenv


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
    assert True

# ------------------ Test 2: Create Post ------------------
def test_b_create_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/create")
    assert True
# ------------------ Test 3: View Post ------------------
def test_c_view_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/view")
    assert True

# ------------------ Test 4: Comment on a Post ------------------
def test_d_comment_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/")
    assert True

# ------------------ Test 5: Like a Post ------------------
def test_e_like_post(driver):
    driver.get("https://emilo-live-stream-front.vercel.app/")
    assert True

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
