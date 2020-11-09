# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:54:36 2020

@author: Gaurav Kumar
"""

# Working with Frames
# Those elements are present in three different frames 
# Get access to those elements by entering into the frames 

# working with radio button and check boxes
from selenium import webdriver

from selenium.webdriver.common.by import By # Using By class 

from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")


driver.switch_to.frame('packageListFrame')
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to.frame('packageFrame')
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to_default_content()

time.sleep(3)
driver.switch_to.frame('classFrame')
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
