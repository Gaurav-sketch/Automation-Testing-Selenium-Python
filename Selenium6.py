# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:22:33 2020

@author: Gaurav Kumar
"""


# working with radio button and check boxes
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("https://fs4.formsite.com/53EL3b/gy6dwijec5/index.html")


check=driver.find_element_by_id('RESULT_RadioButton-11_0')
print("The radio button is selected or not:",check.is_selected())



check2=driver.find_element_by_id('RESULT_CheckBox-12_0')
print("The checkbox button is selected or not:",check2.is_selected())


#https://stackoverflow.com/questions/56212602/error-message-element-click-intercepted
driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-10_0']").click()
check=driver.find_element_by_id('RESULT_RadioButton-10_0')
print("The radio button is selected or not:",check.is_selected())

driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-12_0']").click()

check2=driver.find_element_by_id('RESULT_CheckBox-12_0')
print("The checkbox button is selected or not:",check2.is_selected())


# Working with Dropdowns , find out the group class 
downs=driver.find_element(By.ID,"RESULT_RadioButton-5")

# Then make it kind of select group 
drops=Select(downs)

# =============================================================================
# drops.select_by_visible_text('Morning')
# =============================================================================

# You can select by Index value (0,1,2,3,4)
drops.select_by_index(3)


# =============================================================================
# drops.select_by_value("Radio-1")
# =============================================================================

# This is to get the number of options present in the drop down
len(drops.options)


# To print all the options in the drop down 
# Print the text values for all the options 
for i in drops.options:
    print (i.text)









