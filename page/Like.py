import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_post_only():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # Open app login page
        driver.get("https://your-socialmedia-app.com/login")  # Replace with your app URL

        # --- LOGIN ---
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys("your_username")  # Replace with your username

        driver.find_element(By.NAME, "password").send_keys("your_password")  # Replace with password
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        print("Login completed.")

        # --- CREATE POST ---
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#create-post"))
        ).click()  # Adjust selector for "Create Post" button

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Write something...']"))
        ).send_keys("This is an automated post with media.")

        # Attach image
        driver.find_element(By.CSS_SELECTOR, "input[type='file'][accept*='image']").send_keys(
            r"C:\Users\Rahul\Pictures\test_image.jpg"
        )

        # Attach video
        driver.find_element(By.CSS_SELECTOR, "input[type='file'][accept*='video']").send_keys(
            r"C:\Users\Rahul\Videos\test_video.mp4"
        )

        # Submit post
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print("Post created successfully.")

        time.sleep(5)  # Wait a bit to ensure post is created

    finally:
        driver.quit()
