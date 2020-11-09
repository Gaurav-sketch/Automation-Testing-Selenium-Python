# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:38:38 2020

@author: Gaurav Kumar
"""


# working with input boxes 
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("https://fs4.formsite.com/53EL3b/gy6dwijec5/index.html")


#How many input boxes present on the page 

inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')

print(len(inputboxes))


status=driver.find_element_by_id('RESULT_TextField-2')

print("Displayed or not",status.is_displayed())


status=driver.find_element_by_id('RESULT_TextField-2')

print("Enabled or not",status.is_enabled())



driver.find_element(By.ID,'RESULT_TextField-2').send_keys('GAURAV')


driver.find_element(By.ID,'RESULT_TextField-3').send_keys('KUMAR')



driver.find_element_by_id('RESULT_TextField-4').send_keys('894857635')

#How to get the status of the Input boxes 

