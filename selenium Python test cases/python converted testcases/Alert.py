#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver


# In[22]:


from selenium.webdriver.common.by import By


# In[23]:


from selenium.webdriver.common.action_chains import ActionChains


# In[24]:


import time


# In[25]:


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe",options=chrome_options)
driver.get("http://demo.automationtesting.in/Alerts.html")
time.sleep(3)
d = driver.find_element(By.CLASS_NAME,'btn-danger')
d.click()
alert = driver.switch_to.alert

alert.accept()


# In[ ]:




