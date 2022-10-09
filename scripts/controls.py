from pynput.keyboard import Key
from enum import Enum

class Actions(Enum):
    JUMP = 1
    CROUCH = 2
    DO_NOTHING = 3


def jump(prev_action, controller):
    if prev_action == Actions.JUMP:
        print('already jumping')
    else:
        print('jump')
        controller.press(Key.up)
    return Actions.JUMP

def crouch(prev_action, controller):
    if prev_action == Actions.CROUCH:
        print('already crouching')
    else:
        print('crouch')
        controller.press(Key.down)
    return Actions.CROUCH

def do_nothing(prev_action, controller):
    if prev_action == Actions.DO_NOTHING:
        # print('already doing nothing')
        pass
    else:
        print('do nothing')
        controller.release(Key.up)
        controller.release(Key.down)
    return Actions.DO_NOTHING

def jump_to_start(controller):
    print('jump to start')
    controller.press(Key.up)
    controller.release(Key.up)

def keep_view_on_top(controller):
    controller.press(Key.page_up)