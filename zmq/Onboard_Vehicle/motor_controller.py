import os
import json
import toml
import serial
from sys import platform
from pathlib import Path

robot_config = toml.load(os.environ["DEVICE_CONFIG"])
serial_port = robot_config['peripheral']['serial_port']
baud_rate = robot_config['peripheral']['baud_rate']
#hard-coded to joystick 
with open(os.environ["CONFIG_PATH"] / Path("robot_settings.json")) as rs:
    robot_settings = json.load(rs)['joystick']
message_id = robot_settings["message_id"]

def make_dict(mesg):
    command = {}
    for cmd, val in zip(mesg.commands, mesg.values):
        command[cmd] = val
    return command

def get_default_commands():
    command = {}
    command['brake'] = 0 
    command['throttle'] = 10
    command['steer'] = 0
    command['gear'] = 0
    return command

class MotorController(object):

    def __init__(self, testing=False):
        self.command = robot_settings['defaults']
        self.testing = testing
        if not self.testing and platform in ["linux", "linux2", "win32"]:
            self.ser = serial.Serial(serial_port,baudrate=baud_rate)

    def callback(self, curr_cmd=None):
        if curr_cmd is not None:
            command_dict = make_dict(curr_cmd)
        else:
            command_dict = get_default_commands()
        for cmd, val in self.command.items():
            new_val = command_dict[cmd]
            if val != new_val:
                sent_command = robot_settings[cmd][str(new_val)]
                message = message_id[cmd] + sent_command 
                if not self.testing:
                    self.ser.write(message.encode('utf-8'))
                else:
                    print(message)
                self.command[cmd] = new_val

