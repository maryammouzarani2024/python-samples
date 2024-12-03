from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#perform drag and drop
url="https://the-internet.herokuapp.com/drag_and_drop"

#instantiate webdriver and open a chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#maximize browser window
driver.maximize_window()

#load the web page
driver.get(url)


source=driver.find_element(By.XPATH,'//*[@id="column-a"]')
destination=driver.find_element(By.XPATH,'//*[@id="column-b"]')


action=ActionChains(driver)

action.drag_and_drop(source,destination).perform()


#pause the program for 5 seconds to view the result
sleep(15)

#close the driver
driver.quit()
