#dynamic content

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url="https://the-internet.herokuapp.com/dynamic_controls"

#instantiate webdriver and open a chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#maximize browser window
driver.maximize_window()

#load the web page
driver.get(url)


wait=WebDriverWait(driver,10)

enable_button=driver.find_element(By.XPATH,'//*[@id="input-example"]/button')
enable_button.click()
sleep(3)

disable_button=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input-example"]/button')))
disable_button.click()
sleep(3)




remove_button=driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button')
remove_button.click()
sleep(3)


add=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox-example"]/button')))
add.click()
sleep(3)

checkbox=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox"]')))
checkbox.click()
sleep(3)





#pause the program for 5 seconds to view the result
sleep(15)

#close the driver
driver.quit()
