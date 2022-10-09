
from time import sleep, time
from pynput.keyboard import Controller

from game import close_game, load_game
from random_agent import act_randomly
from controls import Actions, crouch, jump_to_start, keep_view_on_top


def main():
    webdriver = load_game()
    sleep(1)

    controller = Controller()
    keep_view_on_top(controller=controller)
    jump_to_start(controller=controller)    

    prev_action, cur_action = Actions.DO_NOTHING, Actions.DO_NOTHING
    start_time = time()
    playtime_seconds = 7

    while time() - start_time < playtime_seconds:
        cur_action = act_randomly(prev_action=prev_action, controller=controller)
        prev_action = cur_action

    close_game(webdriver=webdriver)

if __name__ == '__main__':
    main()