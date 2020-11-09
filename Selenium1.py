# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:55:51 2020

@author: Gaurav Kumar
"""

# Import the packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#This is to create the driver for chrome 
#This can be tested for different browsers 
driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=r"D:\Spyder\Selenium\geckodriver.exe")

#driver = webdriver.Edge(executable_path=r"D:\Spyder\Selenium\msedgedriver.exe")

#This is to open the specific page you want 
#driver.get("https://www.ucd.ie/connect")

driver.get("http://demo.automationtesting.in/Windows.html")

#You can print the title of the page
print(driver.title)
print(driver.current_url)  #This returns the URL of the page
#print(driver.page_source)  #HTML code of the Page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5) #After clicking keep the window open for 5 sec 

#driver.close() #This is to close the focused browser , one at time incase of multiple browser 

driver.quit()


