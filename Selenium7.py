# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:11:36 2020

@author: Gaurav Kumar
"""

# working with radio button and check boxes
from selenium import webdriver

from selenium.webdriver.common.by import By # Using By class 

from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("https://www.expedia.ie/")

# links contains all the links , these are in a tag
# =============================================================================
# links = driver.find_elements(By.TAG_NAME,'a')   
# 
# print("The number of links present are:",len(links))
# =============================================================================

# =============================================================================
# for link in links:
#     print(link.text)
# 
# 
# =============================================================================

driver.find_element(By.LINK_TEXT,'Trips').click()
# Here you can give partial link also 

# How many links present in webpage and 
# How you can perform actions on those links 
