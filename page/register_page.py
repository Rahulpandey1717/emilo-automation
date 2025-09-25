from selenium import webdriver
from selenium.webdriver.common.by import By
import time

full_name = input("Enter full name: ")
email = input("Enter email: ")
password = input("Enter password: ")

if len(password) < 6:
    print("Password must be at least 6 characters. Registration aborted.")
    exit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://emilo-live-stream-front.vercel.app/login")

driver.find_element(By.CSS_SELECTOR, "a[class='underline text-white hover:text-purple-300']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Full Name']").send_keys(full_name)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']").send_keys(password)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

notifications = driver.find_elements(By.CSS_SELECTOR, "section[aria-label='Notifications Alt+T']")
if notifications:
    print("Registration failed! Notification detected.")
else:
    print("Registration completed successfully!")

driver.quit()
