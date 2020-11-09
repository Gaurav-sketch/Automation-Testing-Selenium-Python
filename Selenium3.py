# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:48:33 2020

@author: Gaurav Kumar
"""

from selenium import webdriver



driver=webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

user_ele=driver.find_element_by_name('email')
print(user_ele.is_displayed())
print(user_ele.is_enabled())


pw_ele=driver.find_element_by_name('passwd')
print(pw_ele.is_displayed())
print(pw_ele.is_enabled())

user_ele.send_keys("gk01021992@gmail.com")
pw_ele.send_keys("Selenium@2020")

driver.find_element_by_name("SubmitLogin").click()

driver.find_element_by_xpath("//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[@title='T-shirts']").click()

tickbox=driver.find_element_by_css_selector("input[value='1_1']")

print("Status of first box",tickbox.is_selected())    

tickbox2=driver.find_element_by_css_selector("input[value='2_1']")

print("status of second box",tickbox2.is_selected()) 


