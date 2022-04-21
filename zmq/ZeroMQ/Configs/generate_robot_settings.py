import json

robot_data = {}
js_brake={
    "0":  "#0200B@",
    "1":  "#0220B@",
    "2":  "#0240B@",
    "3":  "#0260B@",
    "4":  "#0280B@",
    "5":  "#0300B@",
    "6":  "#0320B@"
}

js_throttle={
    "0":  "#0080T@",
    "1":  "#0090T@",
    "2":  "#0100T@",
    "3":  "#0110T@",
    "4":  "#0120T@",
    "5":  "#0130T@",
    "6":  "#0140T@",
    "7":  "#0150T@",
    "8":  "#0160T@",
    "10": "#0000T@"
}

js_steer={
    "0": "#3000S@",
    "1": "#2000S@",
    "2": "#1000S@"
}

js_gear={
    "0": "#FORWA@",
    "1": "#NEUTR@",
    "2": "#REVER@",
}

wheel_brake = {
    "0": "#0200B@",
    "1": "#0220B@",
    "2": "#0240B@",
    "3": "#0260B@",
    "4": "#0280B@",
    "5": "#0300B@",
    "6": "#0320B@",
}

wheel_throttle ={
    "0": "#0080T@",
    "1": "#0090T@",
    "2": "#0100T@",
    "3": "#0110T@",
    "4": "#0120T@",
    "5": "#0130T@",
    "6": "#0140T@",
    "7": "#0150T@"    
}

js_message_id = {
    "brake": "0001",
    "throttle":"0016",
    "steer":"0017",
    "gear": "0002"
} 

js_default = {
   "brake":0, 
   "steer":0,
   "throttle":10,
   "gear":0
 }
robot_data['joystick'] = {}
robot_data['wheel'] = {}

robot_data['joystick']['brake'] = js_brake
robot_data['joystick']['throttle'] = js_throttle
robot_data['joystick']['gear'] = js_gear
robot_data['joystick']['steer'] = js_steer
robot_data['wheel']['brake'] = wheel_brake
robot_data['wheel']['throttle'] = wheel_throttle
robot_data['joystick']['message_id'] = js_message_id 
robot_data['joystick']['defaults'] = js_default

with open("robot_settings.json", "w") as f:
    json.dump(robot_data, f)
    
