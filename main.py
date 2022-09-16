from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://dinorunner.com')

print('hello trex')
sleep(1)