from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller

def load_game():
    print('opening browser...')
    driver = webdriver.Firefox()
    sleep(3)
    
    print('loading page...')
    driver.get('https://dinorunner.com')
    print('page load finished')

    assert driver.title == "Dinosaur T-Rex Game - Chrome Dino Runner Online"


def jump(controller):
    controller.press(Key.space)
    controller.release(Key.space)


if __name__ == '__main__':
    load_game()
    controller = Controller()

    jump(controller=controller)
    sleep(1)
    jump(controller=controller)
    sleep(1)
    jump(controller=controller)

    sleep(1)

