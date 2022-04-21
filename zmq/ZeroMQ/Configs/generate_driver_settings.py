import json
import os, toml

def limit_settings(my_dict, val):
    for k, v in my_dict.items():
        if v > val:
            my_dict[k] = val
    return my_dict

driver_data = {}
js_brake={
    "0.1, 0.3":  0,
    "0.3, 0.4":  1,
    "0.4, 0.5":  2,
    "0.5, 0.6":  3,
    "0.6, 0.7":  4,
    "0.7, 0.8":  5,
    "0.9, 1.0":  6 
}

js_throttle={
    "0.1, 0.2": 0,
    "0.2, 0.3": 1,
    "0.3, 0.4": 2,
    "0.4, 0.5": 3,
    "0.5, 0.6": 4,
    "0.6, 0.7": 5,
    "0.7, 0.8": 6,
    "0.8, 0.9": 7,
    "0.9, 1.0": 8 
}

wheel_brake = {
    "0.95, 0.714":  0,
    "0.714, 0.428": 1,
    "0.428, 0.142": 2,
    "0.142, -0.142": 3,
    "-0.142, -0.428": 4,
    "-0.428, -0.714": 5,
    "-0.714, -1.0": 6,
}

wheel_throttle ={
    "0.95, 0.8": 0,
    "0.8, 0.7": 1,
    "0.7, 0.6": 2,
    "0.6, 0.5": 3,
    "0.5, 0.4": 4,
    "0.4, 0.3": 5,
    "0.3, 0.2": 6,
    "0.2, -1.0": 7    
}

default_dict = {
    "brake": 0,
    "throttle":10,
    "steer":0,
    "gear":0
} 

driver_data['wheel_brake'] = wheel_brake
driver_data['wheel_throttle'] = wheel_throttle
driver_data['default_dict'] = default_dict

driver_config = toml.load(os.environ['DEVICE_CONFIG'])
joystick = driver_config['joystick']
max_brake = joystick.get('brake_max',6)
max_throttle = joystick.get('throttle_max',5)
js_brake = limit_settings(js_brake,max_brake)
js_throttle = limit_settings(js_throttle,max_throttle)
driver_data['js_brake'] = js_brake
driver_data['js_throttle'] = js_throttle

with open("./Configs/driver_settings.json", "w") as f:
    json.dump(driver_data, f)
    
