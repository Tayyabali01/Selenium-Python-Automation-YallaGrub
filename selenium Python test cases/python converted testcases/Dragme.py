#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("C:\\Users\\HP\\Desktop\\7\\DragMe.html")
browser.implicitly_wait(5)
print(browser.title)

source_element = browser.find_element(By.XPATH, '//*[@id="draggable"]/p')
actions = ActionChains(browser)


# In[ ]:




