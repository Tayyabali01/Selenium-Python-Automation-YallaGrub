#!/usr/bin/env python
# coding: utf-8

# In[46]:


from selenium import webdriver


# In[47]:


from selenium.webdriver.common.by import By


# In[48]:


from selenium.webdriver.common.keys import Keys


# In[49]:


from selenium.webdriver.support.ui import Select


# In[50]:


import time 


# In[51]:


#driver=webdriver.Chrome("chromedriver.exe",options=chrome_options)
driver = webdriver.Chrome()
driver.get("https://www.google.com/")


# In[52]:


driver=webdriver.Chrome()
driver.get("C:\\Users\\HP\\Desktop\\1\\CreateAccount.htm")
inputElement = driver.find_element("name","FirstName")
inputElement.send_keys('Ahmed ')
inputElement = driver.find_element("name","MName")
inputElement.send_keys('Ijaz')

inputElement = driver.find_element("name","Lname")
inputElement.send_keys('John')

inputElement = driver.find_element("name", "street")
inputElement.send_keys('No. 425, 3rd Main, 7th Cross, 1st Sector, HSR Layout')

ddelement= Select(driver.find_element("name","city"))
ddelement.select_by_value('Peshawar')


ddelement2 = Select(driver.find_element("name","province"))
ddelement2.select_by_value('ICT Capital')

ddelement2 = Select(driver.find_element("name","province"))
ddelement2.select_by_value('ICT Capital')

ddelement3 = Select(driver.find_element("name", "country"))
ddelement3.select_by_value('Japan')

ddelement4 = driver.find_element("name","male")
ddelement4.click()

ddelement4 = driver.find_element("name","urdu")
ddelement4.click()

ddelement5 = driver.find_element("name","Save")
ddelement5.click()

print("Test Pass")


# In[ ]:




