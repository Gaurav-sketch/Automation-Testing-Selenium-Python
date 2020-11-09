# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:25:33 2020

@author: Gaurav Kumar
"""



# working with radio button and check boxes
from selenium import webdriver

from selenium.webdriver.common.by import By # Using By class 

from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")


driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

#driver.switch_to_alert().accept()  #Close alert window using alert button
driver.switch_to_alert().dismiss()

#Dealing with Alert buttons
