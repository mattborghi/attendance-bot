from selenium import webdriver 
from dotenv import load_dotenv
from time import sleep
import os

# Load env variables
load_dotenv()

user_email = os.environ['USER']
user_pass = os.environ['PASS']

# Configure browser, don't open a new window
browser_options = webdriver.ChromeOptions()
browser_options.headless = True

browser = webdriver.Chrome(options=browser_options)
browser.get(os.environ['URL']) 

# Step 0 select enterprise
browser.find_element_by_link_text(os.environ['ENTERPRISE'] + " employee").click()

# Step 1 fill login
user = browser.find_element_by_id("userNameInput")
user.click()
user.send_keys(user_email)

password = browser.find_element_by_id("passwordInput")
password.click()
password.send_keys(user_pass)
# submit
browser.find_element_by_id("submitButton").click()

# Step 2 Attendance
tooltip = browser.find_elements_by_class_name("tool_tip_btn")
tooltip0 = tooltip[0]
btn_before = tooltip0.get_attribute("innerText")

browser.execute_script("document.getElementById('attendance-logger-widget').click()")

sleep(10)

tooltip = browser.find_elements_by_class_name("tool_tip_btn")
tooltip0 = tooltip[0]
btn_after = tooltip0.get_attribute("innerText")

if (btn_before == "Clockin" and btn_after == "Clockout"):
    print("Attendance registered! 🏢💼")
elif (btn_before == "Clockout" and btn_after == "Clockin"):
    print("You have clocked out! 🏡⛱️")
else:
    print("Attendance error! ⚠️ Try again.")
