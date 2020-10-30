import os
import sys
from selenium import webdriver
from getpass import getpass

path = "C:\\Users\\Projects" #ENTER PATH TO YOUR PROJECTS FOLDER

#Name of New Project
name = str(input("Name of project:"))

#Adding Name To Path
path = path + "\\" + name

#Making Folder
os.makedirs(path)

#Name of Script
nameFile = str(input("Name of Script:"))

#Making Script
open(path + "\\" + nameFile, 'w')

#Login to github and Create Repo
driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe") #ENTER PATH TO YOUR CHROMEDRIVER
driver.get("http://github.com/login")
username = "USERNAME" #ENTER YOUR USERNAME NOT EMAIL, WE USE THE USERNAME LATER
password = "PASSWORD" #ENTER YOUR PASSWORD HERE
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()
driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(name)
driver.find_element_by_css_selector('button.first-in-line').submit()

#Navigate to folder to git init and git commit
os.chdir(path)
os.system('git init')
os.system('git add .')
os.system('git commit -m ("Initial Commit")')
os.system('git remote add origin https://github.com/' + username + "/" + name)
os.system('git branch -M main')
os.system('git push -u origin main')
#os.system('code .') #This is optional, if you want the folder opened in Visual Studio Code and you have it installed then uncomment this line