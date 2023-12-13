#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver


# In[22]:


from selenium.webdriver.common.by import By


# In[23]:


from selenium.webdriver.common.action_chains import ActionChains


# In[24]:


# Creating an instance webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get("C:\\Users\\HP\\Desktop\\3\\ContextClick.html")


driver.refresh()

source= driver.find_element(By.XPATH,'/html/body/div');

action = ActionChains(driver)

action.context_click(source).perform()

##driver.close()


# In[ ]:




