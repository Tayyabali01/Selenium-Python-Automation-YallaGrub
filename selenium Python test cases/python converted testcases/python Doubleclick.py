#!/usr/bin/env python
# coding: utf-8

# In[17]:


from selenium import webdriver


# In[18]:


from selenium.webdriver.common.by import By


# In[19]:


from selenium.webdriver.common.action_chains import ActionChains


# In[20]:


# Creating an instance webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get("C:\\Users\\HP\\Desktop\\2\\DoubleClick.html")
click = driver.find_element(By.XPATH,'/html/body/button')

action = ActionChains(driver)
  
# double click the item
action.double_click(on_element = click)
  
# perform the operation
action.perform()


# In[ ]:




