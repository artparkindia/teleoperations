import toml
import json
import time
import os

device_driver={
    'joystick':('js_brake','js_throttle'),
    'wheel': ('wheel_brake','wheel_throttle')
}

dirname = os.path.dirname(__file__)
config_filename = os.path.join(dirname, 'config_remote.toml')
driver_setting_filename = os.path.join(dirname, 'driver_settings.json')

config_data =  toml.load(config_filename)

device_config = config_data["peripheral"]
button_map = config_data['button_map_td']
command_map = config_data['command']
message_ids = config_data['message_id']

device = device_config.get('device','joystick')
brake_driver, throttle_driver = device_driver[device]

def str_to_tuple(str):
    return tuple(map(float, str.split(', ')))

with open(driver_setting_filename) as ds:
    driver_settings = json.load(ds)
    brake_settings = {str_to_tuple(k):v for k, v in driver_settings[brake_driver].items()}
    throttle_settings = {str_to_tuple(k):v for k, v in driver_settings[throttle_driver].items()}
    default_dict = driver_settings['default_dict']

class RemoteDrive(object):
    def __init__(self):
        self.set_defaults(**default_dict)
        self.last_activity_time = time.time()
        self.uptime = time.time()
        
    def set_defaults(self,**defaults):
        self.steer = defaults['steer']
        self.throttle = defaults['throttle']
        self.brake = defaults['brake']
        self.emergency = False
        self.zero_throttle = True
        self.gear = command_map['NEUTRAL']

    def update_brake_throttle(self, command):
        
        if command > 0.1:
            for (bmin, bmax), target in brake_settings.items():
                if bmin < command < bmax:
                    break
            self.brake = target
        elif command < -0.1:
            self.zero_throttle = False
            if self.gear in [command_map['FORWARD'], command_map['REVERSE']]:
                tval = command * -1 
                for (tmin, tmax), target in throttle_settings.items():
                    if tmin < tval < tmax:
                        break
                self.throttle = target
                
        elif -0.1 < command < 0.1 :
            self.brake = "#0200B@"
            self.throttle = "#0000T@"
            self.zero_throttle = True
    
    def engage_gear(self):
        return not self.emergency and self.zero_throttle
    
    def update_brake_gear(self, button, axis_value=0):

        if button == button_map['emergency']:
            print("Emergency Brake")
            self.throttle = "#0000T@"
            self.gear = command_map['NEUTRAL']
            if not self.emergency:
                self.brake = "#0320B@"
            else:
                self.brake = "#0200B@"
                self.zero_throttle = True if axis_value and (-0.1 < axis_value <0.1) else False
            self.emergency = not self.emergency

        elif button == button_map['neutral'] and self.engage_gear():
            print("Neutral Gear")
            self.throttle = "#0000T@"
            self.gear = command_map['NEUTRAL'] 

        elif button == button_map['forward'] and self.engage_gear():
            print("Forward Gear")
            self.throttle = "#0000T@"
            self.gear = command_map['FORWARD']

        elif button == button_map['reverse'] and self.engage_gear():
            print("Reverse Gear")
            self.throttle = "#0000T@"
            self.gear = command_map['REVERSE']
            self.steer = "#3000S@"
        
        elif button == button_map['steer_left']:
            self.steer = "#2000S@"
        
        elif button == button_map['steer_right']:
            self.steer = "#1000S@"

    def reset_steer(self):
        self.steer = "#3000S@"

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
            self.brake = "#0200B@"
            self.throttle = "#0000T@"
        else:
            right = steer_cmd > 0.04
            left = steer_cmd < -0.04 
            self.update_steer(left, right)
                     
    def get_commands(self):
        
        b = message_ids['brake_msgid'] + self.brake
        t = message_ids['throttle_msgid'] + self.throttle
        s = message_ids['steering_msgid'] + self.steer
        g = message_ids['rf_msgid'] + self.gear
        return b, t, s, g
       



            