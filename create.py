import os
import sys
import time
from selenium import webdriver

driver = webdriver.Safari()
driver.get('https://github.com/login')
login_field = driver.find_element_by_xpath('//*[@id="login_field"]')
login_field.clear()
login_field.send_keys('login')
password_field = driver.find_element_by_xpath('//*[@id="password"]')
password_field.clear()
password_field.send_keys('password')
log_in_btn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
log_in_btn.click()
time.sleep(3)
driver.get('https://github.com/new')
new_repo_name_field = driver.find_element_by_xpath('//*[@id="repository_name"]')
new_repo_name_field.send_keys(sys.argv[1])
time.sleep(2)

def create():
	try: 
		os.makedirs('/Users/piotrzyzinski/pythonProjects/' + sys.argv[1])

	except Exception as error:
		print(error)


create()
