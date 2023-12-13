#!/usr/bin/env python
# coding: utf-8

# In[10]:


from selenium import webdriver


# In[11]:


from selenium.webdriver.common.by import By


# In[12]:


from selenium.webdriver.common.action_chains import ActionChains


# In[13]:


driver = webdriver.Chrome("chromedriver.exe")
driver.get("C:\\Users\\HP\\Desktop\\4\ContextClick.html")
click = driver.find_element(By.XPATH,'/html/body/div')





