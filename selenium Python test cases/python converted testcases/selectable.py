#!/usr/bin/env python
# coding: utf-8

# In[4]:


from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe",options = chrome_options)
driver.get("C:\\Users\\HP\\Desktop\\6\\Selectable.html")

element = driver.find_element("name","zero")
element1 = driver.find_element("name","seven")
element2 = driver.find_element("name","one")


action = ActionChains(driver)

action.click(element).perform()
time.sleep(0.5)
action.click(element1).perform()
time.sleep(0.5)
action.click(element2).perform()


time.sleep(2)
driver.close()


# In[ ]:





# In[ ]:




