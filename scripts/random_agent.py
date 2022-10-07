from random import random

from controls import crouch, do_nothing, jump

def act_randomly(prev_action, controller):
    rand_float = random()
    if rand_float > 0.9999999:
        action = jump
    elif rand_float < 0.0000001:
        action = crouch
    else:
        action = do_nothing
    return action(prev_action=prev_action, controller=controller)
