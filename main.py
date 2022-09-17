from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
sleep(1)
driver.get('https://dinorunner.com')

assert driver.title == "Dinosaur T-Rex Game - Chrome Dino Runner Online"

print('hello trex')
sleep(1)