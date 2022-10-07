
from time import sleep
from pynput.keyboard import Controller

from controls import jump
from game import close_game, load_game


def main():
    webdriver = load_game()
    controller = Controller()

    jump(controller=controller)
    sleep(1)
    jump(controller=controller)
    sleep(1)
    jump(controller=controller)
    close_game(webdriver=webdriver)


if __name__ == '__main__':
    main()