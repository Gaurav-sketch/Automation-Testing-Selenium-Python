# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:49:04 2020

@author: Gaurav Kumar
"""


from selenium import webdriver

from selenium.webdriver.common.by import By # Using By class 

from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

time.sleep(3)

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(3)
#print(driver.current_window_handle)

handles=driver.window_handles   # Create handles and All open browser window 

for h in handles:
    driver.switch_to_window(h)
    print(driver.title)
    if driver.title=='Frames & windows':   #To close the selective window first 
        driver.close()
    
    
driver.quit() # To close all the window open in browser 