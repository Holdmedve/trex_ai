from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller

driver = webdriver.Firefox()
driver.get('https://dinorunner.com')

assert driver.title == "Dinosaur T-Rex Game - Chrome Dino Runner Online"

print('hello trex')
sleep(1)

keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)
sleep(1)
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)
sleep(1)
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

sleep(1)

