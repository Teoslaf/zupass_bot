import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver (e.g., Chrome)
driver = webdriver.Chrome()  # or specify the path like webdriver.Chrome('/path/to/chromedriver')

# Open the webpage
driver.get("https://zupass.org/#/?folder=FrogCrypto")

def perform_login(email, password):
    try:
        email_field = driver.find_element(By.CLASS_NAME, "sc-dLMFU.fDzdpT")  # Change this if needed
        email_field.send_keys(email)

        login_button = driver.find_element(By.CLASS_NAME, "sc-dhKdcB.cFngfw")  # Change this if needed
        login_button.click()
        print("Login button clicked after entering email!")
        time.sleep(2)

        password_field = driver.find_element(By.CLASS_NAME, "sc-dLMFU.sc-hCPjZK.fDzdpT.hHsycu")  # Change this if needed
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        time.sleep(5)
        elements = driver.find_elements(By.CLASS_NAME, "sc-dZoequ.dIEKso")
        elements[2].click()
        print("Login button clicked after entering password!")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

def click_button():
    try:
        button = driver.find_elements(By.CLASS_NAME, "sc-kOPcWz.hgfcYK")
        button[2].click()
        print("Button clicked!")
        print("Clicked at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print(f"An error occurred while clicking the button: {e}")

def perform_click_in_loop():
    while True:
        click_button()
        time.sleep(15 * 60 + 15)  # Sleep for 15 minutes

# Prompt for email and password
email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")

perform_login(email, password)
time.sleep(10)  # Wait for the page to settle after login

# Start the loop to click the button every 15 minutes
perform_click_in_loop()
