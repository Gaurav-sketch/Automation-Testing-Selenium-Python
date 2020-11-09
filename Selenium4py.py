# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:13:54 2020

@author: Gaurav Kumar
"""

#pip install translate
#from translate import Translator

#check=Translator(from_lang='English',to_lang='kannada')
#check.translate('Te amo')

from selenium import webdriver 

from selenium.webdriver.common.by import By

# check for second wait 
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

# =============================================================================
# driver=webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")
# 
# 
# driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
# 
# #Verify the title of the page 
# # Wait for sometime here 
# driver.implicitly_wait(20)  #seconds # Generally at the top and is applicable for all element in page
# 
# assert "Login - My Store" in driver.title
# 
# driver.find_element_by_name("email").send_keys("gk01021992@gmail.com")
# driver.find_element_by_name("passwd").send_keys("Selenium@2020")
# 
# driver.find_element_by_name("SubmitLogin").click()
# =============================================================================


#


driver2 = webdriver.Chrome(executable_path=r"D:\Spyder\Selenium\chromedriver.exe")
 
driver2.implicitly_wait(5)

driver2.maximize_window()


driver2.get("https://www.expedia.com/")

# To find by id 

#driver.find_element_by_id("sdsds").click() this is when ID is present
driver2.find_element_by_xpath("//a[@aria-controls='wizard-flight-pwa']").click()


driver2.find_element_by_css_selector("button[aria-label='Leaving from']").send_keys('SFO')

time.sleep(2)

driver2.find_element_by_css_selector("button[aria-label='Going to']").send_keys('NYC')

time.sleep(2)

driver2.find_element(By.XPATH,"//button[@data-testid='submit-button']").click()



#Explicit wait using expected conditions
wait=WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable((By.XPATH,"//[id@]=""])
    
element.click()

time.sleep(3)

driver.quit()






















# =============================================================================
# driver2.find_element_by_css_selector("button[id='d1-btn']")
# 
# driver2.find_element_by_css_selector("button[id='d2-btn']").send_keys("2020-12-20")
# =============================================================================
# =============================================================================
# driver2.find_element_by_id("d1-btn").send_keys("Nov 21").click()
# driver2.find_element_by_class_name("uitk-new-date-picker-selection-date").send_keys("Wed, Nov 18")
# 
# =============================================================================


# Now find the calendar ,find the tag , clear the field and send the keys

# =============================================================================
# driver2.find_element(By.ID,"Provide the ID name").clear()
# driver2.find_element(By.ID,"Provide the ID name").send_keys("12/10/2018")
# 
# 
# driver2.find_element(By.ID,"Provide the ID name").clear()
# driver2.find_element(By.ID,"Provide the ID name").send_keys("15/10/2018")
# =============================================================================


