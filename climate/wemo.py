from ouimeaux.environment import Environment
import time
import sys


def on_switch(switch):
    print("Switch Found!" + switch.name)

def get_status():
    env = Environment(on_switch)
    env.start()
    env.discover(seconds=1)
    desk = env.get_switch('Wemo Mini')
    state = desk.get_state()
    
    if state == 1:
        state = 'On'        
    elif state == 0:
        state = 'Off'

    return state

def wemo_on():
    env = Environment(on_switch)
    env.start()
    env.discover(seconds=1)
    desk = env.get_switch('Wemo Mini')
    power_on = desk.on()

    return power_on
    
def wemo_off():
    env = Environment(on_switch)
    env.start()
    env.discover(seconds=1)
    desk = env.get_switch('Wemo Mini')
    power_off = desk.off()

    return power_off