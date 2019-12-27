from selenium import webdriver
import time

url = 'https://protonmail.com/signup'
driver = webdriver.Chrome('/goinfre/bnkosi/Desktop/Pythonstuff/pythonstuff/account_create/driver/chromedriver')
driver.get(url)

time.sleep(2)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(2)

driver.find_element_by_id('freePlan').click()

time.sleep(20)

driver.find_element_by_id('username').send_keys('usernameForUser')

time.sleep(2)

driver.find_element_by_id('pasword').send_keys('passwordForUser')

time.sleep(2)

driver.find_element_by_id('paswordc').send_keys('passwordForUser')

time.sleep(2)

driver.find_element_by_class_name('signUpProcess-btn-create').clicl()