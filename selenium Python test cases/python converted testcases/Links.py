#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import urllib3
#import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
broken_links = 0
valid_links = 0

# driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://sofit.ltd/')
 
# links = driver.find_elements_by_css_selector("a")
links = driver.find_elements(By.CSS_SELECTOR, "a")
 
for link in links:
    try:
        request = requests.head(link.get_attribute('href'), data ={'key':'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if (request.status_code == 404):
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")     
    except:
        print("Encountered Some other execption")
print ("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(valid_links) + " valid links")


# In[ ]:




