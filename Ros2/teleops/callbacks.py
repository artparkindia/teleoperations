import pygame
import time
import toml
import os
import sys 

dirname = os.path.dirname(__file__)
config_filename = os.path.join(dirname, 'config_remote.toml')
button_map = toml.load(config_filename)['button_map']

def js_callback(remote_driver, handler, events=[]):
    for event in events: 
        remote_driver.set_uptime = time.time()
        if event.type == pygame.JOYAXISMOTION and not remote_driver.emergency:
            command = handler.get_axis(1)
            remote_driver.update_brake_throttle(command)
        elif event.type == pygame.JOYBUTTONDOWN:
            brake_gear_updated = remote_driver.update_brake_gear(handler)
            if not brake_gear_updated:
                left = handler.get_button(button_map['steer_left'])
                right = handler.get_button(button_map['steer_right'])
                remote_driver.update_steer(left, right)
        elif event.type == pygame.JOYBUTTONUP:
            remote_driver.reset_steer()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() and pygame.KMOD_CTRL:
                print('pygame quit')
    

def wheel_callback(remote_driver, handler, events=None):
    for event in events:  # User did something.
        remote_driver.uptime = time.time()
        if event.type == pygame.JOYAXISMOTION:
            steer = handler.get_axis(0)
            accel = handler.get_axis(2)
            brake = handler.get_axis(3)
            remote_driver.update_wheel_control(steer, accel, brake)                
        if event.type == pygame.JOYBUTTONDOWN:
            if handler.get_button(6):#emergency brake
                remote_driver.set_defaults()
                remote_driver.brake="#320B@"
