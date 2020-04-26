import os
import sys
import time
from selenium import webdriver

path = '/Users/piotrzyzinski/pythonProjects/'
folderName = str(sys.argv[1]) # Linking folder name sending by arg to string
driver = webdriver.Safari() # Defining driver for Safari
file = open('/Users/piotrzyzinski/pythonProjects/projectAutomation/files/git_pass.txt', 'r')
if file.mode == 'r':
	git_login = str(file.readline()).strip()
	git_pass = str(file.readline()).strip()
	
file.close()


def create():
	try: 
		# Creating dir with arg from command	
		os.makedirs(path + folderName)

		# Filling out login form
		driver.get('https://github.com/login')
		
		login_field = driver.find_element_by_xpath('//*[@id="login_field"]')
		login_field.clear()
		login_field.send_keys(git_login)
		
		password_field = driver.find_element_by_xpath('//*[@id="password"]')
		password_field.clear()
		password_field.send_keys(git_pass)
		
		log_in_btn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
		log_in_btn.click()
		
		time.sleep(3) # Probably my internet is slow and i have to wait until page will be fully loaded
		
		# Creating new repo with arg from command
		driver.get('https://github.com/new')
		new_repo_name_field = driver.find_element_by_xpath('//*[@id="repository_name"]')
		new_repo_name_field.send_keys(sys.argv[1])
		
		time.sleep(2) # Waiting for check repo's name availability
		
		new_repo_btn = driver.find_element_by_css_selector('button.first-in-line')
		new_repo_btn.submit()
		
		time.sleep(3) # Waiting for submit data
		driver.close()

	except Exception as error:
		print(error)


create()
