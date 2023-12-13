from xml.dom.minidom import Element
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import datetime
import random
import time

print(selenium.__version__)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://devbranch.yallagrub.com/')
#Login Wakha Albarsha
LoginEmail_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
LoginEmail_textfield.click()
LoginEmail_textfield.send_keys("tayyabalishansa123@gmail.com")
time.sleep(2)

Password_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
Password_textfield.click()
Password_textfield.send_keys("1234512345")
time.sleep(2)

rememberMe_Checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='rememberMe']")))
rememberMe_Checkbox.click()
time.sleep(2)

Login_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Login_Button.click()
time.sleep(2)

#Click on pending Orders 
PendingOrder_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='Pending']")))
PendingOrder_button.click()
time.sleep(2)



# Click on the first pending order in the dialog box
FirstOrderPending_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstOrderPending_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)


# Find and print the customer details using XPath
ordernumber_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Order#')]")
ordernumber = ordernumber_element.text 
expectedtime_element= driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Expected Time')]")
expectedtime = expectedtime_element.text
customername_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-8 fw-600 text-gray-3']")
customername= customername_element.text
customerphone_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-7 text-gray-5']")
customerphone= customerphone_element.text

print("Order Number:", ordernumber)
print("Expected Time:", expectedtime)
print("Customer Name:", customername)
print("Customer Phone:", customerphone)

# Get the current date and time
current_datetime = datetime.datetime.now()

formatted_current_time = current_datetime.strftime("%H:%M on %d %b %Y")

print("Current Date:", formatted_current_time)

# Click the first preferred time checkbox
SelectFirstPreferredTime_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
)
SelectFirstPreferredTime_checkbox.click()

# Get the value of the selected preferred time
selected_preferred_time_element = driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
selected_preferred_time = selected_preferred_time_element.text

# Print the value of the selected preferred time
print("Selected Preferred Time:", selected_preferred_time)


time.sleep(10)

if formatted_current_time > selected_preferred_time:

 #Code for canceling the order
    CancelOrder_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Order']")))
    CancelOrder_btn.click()
    time.sleep(3)
    CancelOrderSuccess_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel and Refund']")))
    CancelOrderSuccess_btn.click()
    print("order cancel successfully", CancelOrderSuccess_btn)
    time.sleep(5)

#Refund screen 
    YesFullRefund_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='fullRefund']")))
    YesFullRefund_Checkbox.click()
   
    SelectReason1_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='reason1']")))
    SelectReason1_Checkbox.click()
    time.sleep(2)

    Refund_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Refund']")))
    Refund_btn.click()
    time.sleep(5)
    driver.refresh()
else:
#Code for Accepting the order
    SelectFirstPrefferedtime_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
    )
    SelectFirstPrefferedtime_checkbox.click()
    selected_preferred_time_element = driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
    selected_preferred_time = selected_preferred_time_element.text
    print("Selected Preferred Time:", selected_preferred_time)
    time.sleep(2)

    # Locate the dropdown element
    SelectTable_dialogbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tableNumbers']")))
    time.sleep(3)

    # Create a Select object
    select = Select(SelectTable_dialogbox)

    # Select the first item using index (index starts from 0)
    desired_index = 1
    select.select_by_index(desired_index)
    time.sleep(3)

    AcceptOrder_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept Order']")))
    AcceptOrder_btn.click()
    time.sleep(10)

#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(8)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(5)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(3)

print("working fine", FirstRunningOrders_button)
time.sleep(3)

order_type_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Order Type')]/following-sibling::div")))
ordertype = order_type_element.text
restaurant_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Restaurant')]/following-sibling::div")))
restaurant= restaurant_element.text
branch_name_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Branch Name')]/following-sibling::div")))
branchname= branch_name_element.text
date_of_order_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Date Of Order')]/following-sibling::div")))
date_of_order= date_of_order_element.text
table_number_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Table Number')]/following-sibling::div")))
table_number= table_number_element.text
guests_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Guests')]/following-sibling::div")))
guests= guests_element.text
pos_i_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'POS I')]/following-sibling::div")))
pos_i= pos_i_element.text 

# Print the extracted information
print("ordertype:" , ordertype)
print("Restaurant:", restaurant)
print("Branch Name:", branchname)
print("Date Of Order:", date_of_order)
# print("Time to serve:", time_to_serve)
print("Table Number:", table_number)
print("Guests:", guests)
print("POS I:", pos_i)
time.sleep(2)

SendtoKitchen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send To Kitchen']")))
SendtoKitchen_button.click()
time.sleep(3)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(2)
Readytoserve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ready to Serve']")))
Readytoserve_button.click()
time.sleep(2)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(2)

Serve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Serve']")))
Serve_button.click()
time.sleep(2)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(2)

MarkCopleted_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Mark Completed']")))
MarkCopleted_button.click()
time.sleep(2)

driver.refresh()
HistoryOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='History']")))
HistoryOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstHistoryorder_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstHistoryorder_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(2)

Refund1_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn btn-outline-pink me-3']")))
Refund1_button.click()
time.sleep(2)


#Refund screen 
YesFullRefund_Checkbox = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//input[@id='fullRefund']")))
YesFullRefund_Checkbox.click()
   
SelectReason1_Checkbox = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//input[@id='reason1']")))
SelectReason1_Checkbox.click()
time.sleep(2)

Refund_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Refund']")))
Refund_btn.click()
time.sleep(2)

driver.refresh()
RefundedOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Refunded']")))
RefundedOrders_button.click()
time.sleep(2)

FirstRefundedOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRefundedOrders_button.click()
time.sleep(2)
Close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn btn-outline-pink me-3']")))
Close_button.click()
time.sleep(2)
driver.refresh()
time.sleep(3)
ExportOrderFile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-pink btn-sm']")))
ExportOrderFile_button.click()
# Wait for some time to allow the action to take place
time.sleep(2)

# Get the value of the class attribute
class_attribute_value = ExportOrderFile_button.get_attribute("class")

Logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Logout']//*[name()='svg']")))
Logout_button.click()

time.sleep(100)







