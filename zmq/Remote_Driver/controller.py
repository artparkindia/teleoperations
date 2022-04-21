import os
import toml
import json
import time
from pathlib import Path

device_driver={
    'joystick':('js_brake','js_throttle'),
    'wheel': ('wheel_brake','wheel_throttle')
}

driver_config_path = os.environ["CONFIG_PATH"] / Path("driver_config.toml")
device_config = toml.load(driver_config_path)["peripheral"]
device = device_config.get('device','joystick')
brake_driver, throttle_driver = device_driver[device]

def str_to_tuple(str):
    return tuple(map(float, str.split(', ')))

with open(os.environ['CONFIG_PATH'] / Path('driver_settings.json')) as ds:
    driver_settings = json.load(ds)
    brake_settings = {str_to_tuple(k):v for k, v in driver_settings[brake_driver].items()}
    throttle_settings = {str_to_tuple(k):v for k, v in driver_settings[throttle_driver].items()}
    default_dict = driver_settings['default_dict']

class RemoteDrive(object):
    def __init__(self):
        self.set_defaults(**default_dict)
        self.last_activity_time = time.time()
        self.uptime = time.time()
        self.prev_cmd = {}
         
    def set_defaults(self,**defaults):
        self.steer = defaults['steer']
        self.throttle = defaults['throttle']
        self.brake = defaults['brake']
        self.gear = defaults['gear']
        self.new_zero_pos = True
        self.emergency = False
        self.zero_throttle = True

    def update_brake_throttle(self, command):
        if command > 0.1:
            for (bmin, bmax), target in brake_settings.items():
                if bmin < command < bmax:
                    break
            self.brake = target
            self.new_zero_pos = True
        elif command < -0.1:
            self.zero_throttle = False
            tval = command * -1 
            for (tmin, tmax), target in throttle_settings.items():
                if tmin < tval < tmax:
                    break
            self.throttle = target
            self.new_zero_pos = True
        elif -0.1 < command < 0.1 and self.new_zero_pos:
            self.brake = 0 
            self.throttle = 10 
            self.new_zero_pos = False
            self.zero_throttle = True

    def update_brake_gear(self, handler):
        old_brake, old_gear = self.brake, self.gear
        if handler.get_button(2):
            print("Emergency Brake")
            self.gear = 1 
            self.throttle = 10 
            self.brake = 6 
            self.emergency = not self.emergency            
        if handler.get_button(1) and self.zero_throttle:
            print("Neutral Gear")
            self.gear = 2 
        if handler.get_button(3) and self.zero_throttle:
            print("Forward Gear")
            self.gear = 0 
        if handler.get_button(0) and self.zero_throttle:
            print("Reverse Gear")
            self.gear = 1 
        return old_gear != self.gear and old_brake != self.brake

    def update_steer(self, left_turn, right_turn):
        if left_turn:
            self.steer = 1 
        elif right_turn:
            self.steer = 2 
    
    def reset_steer(self):
        self.steer = 0 

    def update_wheel_control(self, steer_cmd, accel_cmd, brake_cmd):
        if brake_cmd < 0.95:
            for (bmax, bmin), target in brake_settings.items():
                if bmax > brake_cmd > bmin:
                    break
            self.brake = target   
        elif accel_cmd < 0.95:
            for (amax, amin), target in brake_settings.items():
                if amax > accel_cmd > amin:
                    break
            self.throttle = accel_cmd
        elif 0.97 < accel_cmd < 0.95:
            self.brake = 0 
            self.throttle = 0
        else:
            right = steer_cmd > 0.04
            left = steer_cmd < -0.04 
            self.update_steer(left, right)
                     
    def get_commands(self):
        command_dict = {}
        command_dict['brake'] = self.brake
        command_dict['throttle'] = self.throttle
        command_dict['steer'] = self.steer
        command_dict['gear'] = self.gear
        return command_dict

    def command_change(self, curr_cmd):
        if self.prev_cmd != curr_cmd:
            self.prev_cmd = curr_cmd
            return True
        else:
            return False
       



            
