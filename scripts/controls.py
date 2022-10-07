from pynput.keyboard import Key, Controller

def jump(controller):
    controller.press(Key.up)
    controller.release(Key.up)

def crouch(controller):
    controller.press(Key.space)
    controller.release(Key.space)