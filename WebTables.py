# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 01:03:08 2020

@author: Gaurav Kumar
"""

# working with web tables 
# We can extract particular row and column from the webpage 

from selenium import webdriver

from selenium.webdriver.common.by import By # Using By class 

from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("https://www.toolsqa.com/selenium-webdriver/handle-dynamic-webtables-in-selenium-webdriver/")


# Count number of rows 

rows=len(driver.find_elements_by_xpath("//*[@id='post-2924']/div[1]/div/div[2]/div/div/div/div/table/tbody/tr"))


print(rows)

rows2=len(driver.find_elements_by_xpath("//*[@id='post-2924']/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[1]/th"))

print(rows2)

# Iterate the rows and number of columns to extract the elements out of the table

print("Automation Tool"+"    "+"Licensing"+"   "+"Market response")
for i in range(2,rows+1):
    for c in range(1,rows2+1): 
        value=driver.find_element_by_xpath("//*[@id='post-2924']/div[1]/div/div[2]/div/div/div/div/table/tbody/tr["+str(i)+"]/td["+str(c)+"]")
        print(value.text,end="           ")
    print()




