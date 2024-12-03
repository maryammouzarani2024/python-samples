from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


url="https://saucelabs.com/lp-sauce-labs-vs-lambdatest"

#instantiate webdriver and open a chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#maximize browser window
driver.maximize_window()

#load the web page
driver.get(url)

#find the first name field in the page using its XPath
first_name=driver.find_element(By.XPATH,'//*[@id="FirstName"]')
#fill out the first name field
first_name.send_keys("Mary")


#same for other fields in the form
email=driver.find_element(By.XPATH,'//*[@id="Email"]')
email.send_keys("mary@sample.com")

#same for other fields in the form
last_name=driver.find_element(By.XPATH,'//*[@id="LastName"]')
last_name.send_keys("mzrn")


#same for other fields in the form
company=driver.find_element(By.XPATH,'//*[@id="Company"]')
company.send_keys("myCompany")


#country is a drop-down list
country = Select(driver.find_element(By.XPATH,'//*[@id="Country"]'))
country.select_by_visible_text("Albania")

#agree is a checkbox
agree=driver.find_element(By.XPATH,'//*[@id="LblmktoCheckbox_44876_0"]')
agree.click()



#finally the submit button
submit=driver.find_element(By.XPATH,'//*[@id="mktoForm_3470"]/div[18]/span/button')
submit.click()

#scroll down to 200 units to view the lower part of the page
driver.execute_script("window.scrollTo(0,window.scrollY+200)")


#pause the program for 5 seconds to view the result
sleep(15)

#close the driver
driver.quit()
