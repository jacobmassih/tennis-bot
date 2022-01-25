from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options=options,executable_path=PATH)

driver.get("https://loisirs.montreal.ca/IC3/#/U6510/search/?searchParam=%7B%22filter%22:%7B%22isCollapsed%22:false,%22value%22:%7B%22startTime%22:%222021-05-14T08:00:07.556-04:00%22,%22endTime%22:%222021-05-14T09:00:07.560-04:00%22,%22dates%22:%5B%222021-05-14T00:00:00.000-04:00%22,%222021-05-15T00:00:00.000-04:00%22,%222021-05-16T00:00:00.000-04:00%22,%222021-05-17T00:00:00.000-04:00%22,%222021-05-18T00:00:00.000-04:00%22,%222021-05-19T00:00:00.000-04:00%22,%222021-05-20T00:00:00.000-04:00%22,%222021-05-21T00:00:00.000-04:00%22,%222021-05-22T00:00:00.000-04:00%22,%222021-05-23T00:00:00.000-04:00%22,%222021-05-24T00:00:00.000-04:00%22,%222021-05-25T00:00:00.000-04:00%22,%222021-05-26T00:00:00.000-04:00%22,%222021-05-27T00:00:00.000-04:00%22,%222021-05-28T00:00:00.000-04:00%22,%222021-05-29T00:00:00.000-04:00%22,%222021-05-30T00:00:00.000-04:00%22%5D,%22siteId%22:792%7D%7D,%22search%22:%22%233%22,%22sortable%22:%7B%22isOrderAsc%22:true,%22column%22:%22facility.name%22%7D%7D&bids=20,55&hasBoroughFilter=true")

WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.ID, "U2000_BusyIndicator")))
time.sleep(3)
connection_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable( (By.ID, 'u2000_btnSignIn') ))
connection_button.click()

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable( (By.ID, 'loginForm:username') ))
username.send_keys("ENTER_EMAIL_ADDRESS_HERE")

password = driver.find_element_by_id("loginForm:password")
password.send_keys("ENTER_PASSWORD_HERE")

connect_button = driver.find_element_by_id("loginForm:loginButton")
connect_button.click()

plus_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable( (By.ID, 'u6510_btnButtonReservation0') ))
plus_button.click()


WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='busy-indicator']")))
selection = WebDriverWait(driver,30).until(EC.element_to_be_clickable( (By.ID, 'u3600_btnSelect0') ))
selection.click()

WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.ID, "U2000_BusyIndicator")))
confirm = WebDriverWait(driver,30).until(EC.element_to_be_clickable( (By.ID, 'u3600_btnCartMemberCheckout') ))
confirm.click()

WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='busy-indicator']")))
complete = WebDriverWait(driver,30).until(EC.element_to_be_clickable( (By.ID, 'u3600_btnCartShoppingCompleteStep') ))
complete.click()
