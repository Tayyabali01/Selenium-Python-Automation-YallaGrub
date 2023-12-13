#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver


# In[8]:


from selenium.webdriver.common.by import By


# In[9]:


from selenium.webdriver.common.action_chains import ActionChains


# In[11]:


# Code for Drag and Drops

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("C:\\Users\\HP\\Desktop\\5\\DragAndDrop.html")
browser.implicitly_wait(5)
print(browser.title)


source_element = browser.find_element(By.XPATH, "/html/body/div[1]/p")
target_element = browser.find_element(By.XPATH,"/html/body/div[2]")
actions = ActionChains(browser)
actions.drag_and_drop(source_element,target_element).perform()


# In[ ]:




