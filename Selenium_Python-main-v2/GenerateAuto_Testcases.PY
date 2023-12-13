from xml.dom.minidom import Element
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import selenium
# import cv2
# import pyautogui
# import os
# import base64
# import random
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import Select
# import numpy as np
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

# Set the path to the Chrome extension file
extension_path = r"C:\Selenium_Python-YallaGrub\LOOPJJEGNLCCNHGFEHEKECPANPMIELCJ_1_6_8_0 (2).crx"

# Create ChromeOptions and add the extension
chrome_options = Options()
chrome_options.add_extension(extension_path)

# Create a WebDriver object using ChromeOptions
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

driver.get('chrome-extension://loopjjegnlccnhgfehekecpanpmielcj/testCaseStudio/studioWindow.html')

# Open a new tab using JavaScript
driver.execute_script("window.open('', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
driver.get('https://devuser.yallagrub.com/')
Lapa_Eatery = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[contains(@class,'mx-4')]/div[contains(@class,'flex flex-col md:flex-row md:flex-wrap')]/div[1]/div[1]/div[1]")))
Lapa_Eatery.click()
# payloadCheckout:{"info":{"order":{}}}
def get_requests():
    url = ('https://dev-user.yallagrub.com/api/branches/getrestaurantbranches/651c423f34836b644dbc0fd9')
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Restaurant Information is ===>", json_str)
# Load Json Data
    response = json.loads(json_str)
# Extract _id
    RestaurantName = response[0]["restaurantName"]
    print("RestaurantName is ----->", RestaurantName)
    Branch_Name = response[0]["name"]
    print("BranchName is -----> :", Branch_Name)

# Extract _Timings From Responce
    Monday_Timings = response[0]["timings"]["monday"]
    print("Monday_Timings -------------------------------->>>>>>>>>>>>>>>>>>>>:", Monday_Timings)
    Tuesday_Timings = response[0]["timings"]["tuesday"]
    print("Tuesday_Timings -------------------------------->>>>>>>>>>>>>>>>>>>>:", Tuesday_Timings)
    Wednesday_Timings = response[0]["timings"]["wednesday"]
    print("Wednesday_Timings-------------------------------->>>>>>>>>>>>>>>>>>>>:", Wednesday_Timings)
    Thursday_Timings = response[0]["timings"]["thursday"]
    print("Thursday_Timings -------------------------------->>>>>>>>>>>>>>>>>>>>:", Thursday_Timings)
    Friday_Timings = response[0]["timings"]["friday"]
    print("Friday_Timings -------------------------------->>>>>>>>>>>>>>>>>>>>:", Friday_Timings)
    Saturday_Timings = response[0]["timings"]["saturday"]
    print("Saturday_Timings-------------------------------->>>>>>>>>>>>>>>>>>>>:", Saturday_Timings)
    Sunday_Timings = response[0]["timings"]["sunday"]
    print("Sunday_Timings -------------------------------->>>>>>>>>>>>>>>>>>>>:", Sunday_Timings)

    Tip_Setting = response[0]["branchTip"]
    print("Tip_Setting From Branch side is ----->>>:", Tip_Setting)
    # user_id = json_str["_id"]
    # print("Restaurant Information is ===>", user_id)

#CALLING SECTION 
get_requests()

LapaEatery_Item = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div/div[@class='md:my-8']/div[1]/div[1]")))
LapaEatery_Item.click()

ChiaPudding_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='Chia Pudding']")))
ChiaPudding_btn.click()
time.sleep(2)

Select1_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex justify-between items-center menu-quantity-items']//div[3]//*[name()='svg']")))
Select1_btn.click()
time.sleep(2)

Addtocart_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex w-full bg-pink text-white py-3 px-4 rounded justify-between custom-btn-color']")))
Addtocart_btn.click()
time.sleep(2)

# Scroll down to the half page
driver.execute_script("window.scrollTo(0, (window.scrollY + window.innerHeight) / 2);")
time.sleep(2)

# If "AddTip_btn" exists (i.e., tip is not added yet), click on it
try:
    AddTip_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='+5 AED']")))
    AddTip_btn.click()
    print("Value of AddTip_btn:", AddTip_btn.text)
    time.sleep(2)
except:
    print("1st SelectPrefferedtime_textbox not found")

# Click on "Let's Plan Your Order" button
LetsPlanYourOrder_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'bg-pink my-5 py-4 w-full text-white rounded-md')]")))
LetsPlanYourOrder_btn.click()
time.sleep(5)

#Create Reservation Screen
NoOfGuests_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
NoOfGuests_textbox .click()
NoOfGuests_textbox .clear()
NoOfGuests_textbox .send_keys("10")
time.sleep(2)

#SelectDate
SelectDate_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-xs']")))
SelectDate_textbox .click()

#To get automatic date for today
def get_ordinal_indicator(day):
    if 11 <= day <= 13:
        return 'th'
    else:
        last_digit = day % 10
        if last_digit == 1:
            return 'st'
        elif last_digit == 2:
            return 'nd'
        elif last_digit == 3:
            return 'rd'
        else:
            return 'th'

# Get today's date
today = datetime.date.today()

# Get the day of the week and ordinal indicator
day_of_week = today.strftime("%A")
day = today.day
ordinal_indicator = get_ordinal_indicator(day)

# Build the aria-label string
aria_label = f"Choose {day_of_week}, {today.strftime('%B')} {day}{ordinal_indicator}, {today.year}"

# Build the XPath with the dynamically obtained date
xpath = f"//div[contains(@aria-label, '{aria_label}')]"

# Click on the button for today's date
Selecttodaydate_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#print(xpath)
Selecttodaydate_btn.click()


# Selecttodaydate_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label,'Choose Thursday, June 8th, 2023')]")))
# Selecttodaydate_btn .click()

time.sleep(2)

#Select Preffered time
try:
    SelectPrefferedtime_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Preferred Time')]")))
    SelectPrefferedtime_textbox .click()
    time.sleep(2)
except:
    print("1st SelectPrefferedtime_textbox not found")
else:
    print("1st SelectPrefferedtime_textbox Found and clicked successfully")

# Locate the dropdown options and select the option by index
    options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
    index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
    if options:
        options[index].click()
        print("Option selected successfully", index)
    else:
        print("But Options not found and also noy clickable")

time.sleep(5)


#Select 2nd Time Slot
try:
    Select2ndTimeSlot_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='headlessui-listbox-button-:r8:']//span[@class='flex items-center']")))
    Select2ndTimeSlot_textbox .click()
except:
    print("2nd SelectPrefferedtime_textbox not found")
else:
    print("2nd SelectPrefferedtime_textbox Found and clicked successfully")
# Locate the dropdown options and select the option by index
    options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
    index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
    if options:
        options[index].click()
        print("Option selected successfully", index)
    else:
        print("But Options not found and also noy clickable")


#Select 3rd Time Slot
try:
    Select3rdTimeSlot_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Time Slot Option')]")))
    Select3rdTimeSlot_textbox .click()
except:
    print("3rd SelectPrefferedtime_textbox not found")
else:
    print("3rd SelectPrefferedtime_textbox Found and clicked successfully")
# Locate the dropdown options and select the option by index
    # Locate the dropdown options and select the option by index
    options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
    index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
    if options:
        options[index].click()
        print("Option selected successfully", index)
    else:
        print("But Options not found and also noy clickable")

try:
    NEXT_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center justify-center']")))
    NEXT_btn .click()
except:
    print("Next button is not available")
else:
    print("Next button is available and its working fine")


time.sleep(10)



#Your Information
FullName_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='clientFullName']")))
time.sleep(2)
FullName_Textfield .click()
FullName_Textfield .send_keys("Tayyab ali")

Email_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=' ']")))
Email_Textfield.click()
time.sleep(2)
Email_Textfield.send_keys("tayyabalisa123@gmail.com")

PhoneNumber_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='1 (702) 123-4567']")))
PhoneNumber_Textfield.click()
time.sleep(2)
PhoneNumber_Textfield.send_keys("7373474775")

Checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Checkout']")))
Checkout_btn.click()
time.sleep(10)

EnterOTP_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='otp1']")))
EnterOTP_Textfield.click()
EnterOTP_Textfield.send_keys("55690")

Verify_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Verify']")))
Verify_btn.click()
time.sleep(10)

def Post_requests():
    Post_URL = ('https://dev-user.yallagrub.com/api/users/registeruser')
    data = {
    "info": {
        "order": {
            "branchId": "651c53fa955adce2e46a2890",
            "branchName": "Jumeirah",
            "branchImage": "https://prod-yallagrub.s3.me-central-1.amazonaws.com/allergen-image-1696505184177.png",
            "branchLocation": {
                "lat": 25.171176610038305,
                "lng": 55.2166905
            },
            "menuId": "651c53fa955adce2e46a2893",
            "restaurantId": "651c423f34836b644dbc0fd9",
            "restaurantName": "Lapa Eatery",
            "restaurantLogo": "https://prod-yallagrub.s3.me-central-1.amazonaws.com/menuItem-1696834929402.png",
            "restaurantPrefix": "LER",
            "clientFullName": "",
            "clientEmail": "",
            "clientContactNumber": "",
            "dateOfOrder": "04 Dec 2023",
            "orderItems": [
                {
                    "_id": "65f455bc-8c76-4468-a798-176826bc708c",
                    "name": "Chia Pudding",
                    "price": "62.00",
                    "description": "Chia Pudding topped with homemade dates granola and mixed berries. / NUTRITION FACTS , Calories: 259, Total fat: 14g, Saturated fat: 6g, Trans fat: 0g, Cholesterol: 0mg, Sodium: 0.06g, Total carbohydrates: 31g, Dietary fiber: 9g, Natural Sugars 16g, Protein: 6g,",
                    "categories": [
                        "Breakfast"
                    ],
                    "allergens": [],
                    "image1": "https://prod-yallagrub.s3.me-central-1.amazonaws.com/menuItem-1696353135142.jpg",
                    "image2": "",
                    "image3": "",
                    "image4": "",
                    "discount": 0,
                    "discountType": "Absolute",
                    "discountedPrice": 62,
                    "popular": False,
                    "available": True,
                    "inStock": True,
                    "dineIn": True,
                    "pickup": True,
                    "quantity": 1,
                    "allModifiersPrice": 0,
                    "priceAlongWithModifiers": 62,
                    "totalPrice": 62,
                    "orderItemNotes": "",
                    "allModifiersString": "",
                    "innerId": "e768ea12-42d3-4597-83a6-8d5aa42cef62",
                    "modifiers": [],
                    "itemStatus": "Pending"
                }
            ],
            "subTotal": 62,
            "vAT": 0,
            "tIP": 0,
            "branchTip": {
                "tipType": "Flexible",
                "tipPercentage": 0
            },
            "promoCode": "",
            "promoCodeDiscount": 0,
            "grandTotal": 62,
            "noOfGuests": 1,
            "orderNotes": "",
            "orderStatus": "Pending",
            "orderType": "Pre Order",
            "orderMenuType": "dineIn",
            "currency": "AED",
            "branchNotifications": [],
            "orderNumber": "",
            "selectedFacilities": [],
            "timeConfirmedByRestaurant": "",
            "orderCancellationDetails": {},
            "preferredTimeSlot": "16:15",
            "timeSlotOptionOne": "16:30",
            "timeSlotOptionTwo": "16:45",
            "paymentIntentId": "pi_3OJZjSCXz1vuaM390CipR5YU"
        },
        "clientFullName": "Tayyab",
        "clientEmail": "tayyabalisa123@gmail.com",
        "clientContactNumber": "971538784378"
    }
}
    response = requests.post(Post_URL, '', data)
    # assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("Restaurant Information is ===>", json_str)
    return json_str

PostApiResponse = Post_requests()

# print("PostApiResponse is ===>", PostApiResponse)
#Debit Card Information 


iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

# Wait for the input field to be clickable and enter the card number
CardNumbers_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="number"]')))
CardNumbers_Textfield.click()
CardNumbers_Textfield.send_keys("4242 4242 4242 4242")
time.sleep(2)
# Switch back to the main content
driver.switch_to.default_content()


iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

Expiration_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="expiry"]')))
Expiration_Textfield.click()
Expiration_Textfield.send_keys("1256")
time.sleep(2)

driver.switch_to.default_content()

iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

CVC_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="cvc"]')))
CVC_Textfield.click()
CVC_Textfield.send_keys("776")
time.sleep(2)

driver.switch_to.default_content()

PayNow_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='button-text']")))
PayNow_btn.click()
time.sleep(2)

TrackOrder_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Track order']")))
TrackOrder_btn.click() 
time.sleep(2)

driver.execute_script("window.scrollTo(0, (window.scrollY + window.innerHeight) / 2);")

time.sleep(2)



# Parse the JSON data
api_data = json.loads(PostApiResponse)

# Extract relevant information
token = api_data.get("token")
order_number = api_data["order"]["orderNumber"]
branch_name = api_data["order"]["branchName"]
client_contact_number = api_data["order"]["clientContactNumber"]
client_email = api_data["order"]["clientEmail"]
client_full_name = api_data["order"]["clientFullName"]
date_of_order = api_data["order"]["dateOfOrder"]
restaurant_name = api_data["order"]["restaurantName"]
sub_total = api_data["order"]["subTotal"]
tip = api_data["order"]["tIP"]
grand_total = api_data["order"]["grandTotal"]
no_of_guests = api_data["order"]["noOfGuests"]
order_notes = api_data["order"]["orderNotes"]
preferred_time_slot = api_data["order"]["preferredTimeSlot"]
time_slot_option_one = api_data["order"]["timeSlotOptionOne"]
time_slot_option_two = api_data["order"]["timeSlotOptionTwo"]
promo_code = api_data["order"]["promoCode"]
promo_code_discount = api_data["order"]["promoCodeDiscount"]
currency = api_data["order"]["currency"]
order_status = api_data["order"]["orderStatus"]
order_type = api_data["order"]["orderType"]
order_menu_type = api_data["order"]["orderMenuType"]

# Now you can use these variables in your Selenium automation logic
# For example, let's print them
print("Token:", token)
print("Order Number:", order_number)
print("Branch Name:", branch_name)
print("Client Contact Number:", client_contact_number)
print("Client Email:", client_email)
print("Client Full Name:", client_full_name)
print("Date of Order:", date_of_order)
print("Restaurant Name:", restaurant_name)
print("Sub Total:", sub_total)
print("Tip:", tip)
print("Grand Total:", grand_total)
print("No of Guests:", no_of_guests)
print("Order Notes:", order_notes)
print("Preferred Time Slot:", preferred_time_slot)
print("Time Slot Option One:", time_slot_option_one)
print("Time Slot Option Two:", time_slot_option_two)
print("Promo Code:", promo_code)
print("Promo Code Discount:", promo_code_discount)
print("Currency:", currency)
print("Order Status:", order_status)
print("Order Type:", order_type)
print("Order Menu Type:", order_menu_type)



# order_number_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Number")]/following-sibling::div[@class="h7 font-semibold"]')
# order_number = order_number_element.text

# order_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Type")]/following-sibling::div[@class="h7 font-semibold"]')
# order_type = order_type_element.text

# guest_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Guests")]/following-sibling::div[@class="h7 font-semibold"]')
# guest = guest_element.text

# Table_No_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Table No")]/following-sibling::div[@class="h7 font-semibold"]')
# Table_No = Table_No_element.text

# Date_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Date")]/following-sibling::div[@class="h7 font-semibold"]')
# Date_type = Date_type_element.text

# Time_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Time")]/following-sibling::div[@class="h7 font-semibold"]')
# Time_type = Time_type_element.text

# print("Order Number:", order_number)
# print("Order Type:", order_type)
# print("Guest:", guest)
# print("Table_No:", Table_No)
# print("Date_type:", Date_type)
# print("Time_type:", Time_type)

# Switch back to the Test case studio Tab
driver.switch_to.window(driver.window_handles[0])
print("back on test case studio page")
time.sleep(5)
Test_CaseName = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadFileName"]/input'))
)
Test_CaseName.send_keys("User Dine In Test Case")
time.sleep(3)

try:
    GeneratTestcase_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="save_btn"]'))
    )
    GeneratTestcase_btn.click()
except:
    print("Test Cases not Generated due to wrong xpath")
else: 
    print("Test Cases Generated and Downloaded Successfully")
time.sleep(10)

