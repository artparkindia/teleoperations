import sys
import os
import pygame
import time
import toml
import Schema
import numpy as np
import pandas as pd
from pathlib import Path
from Common.bus import Bus, Sync
from Remote_Driver.callbacks import *
from Remote_Driver.controller import RemoteDrive

"""
In this test code we are testing basic vehicle control over the network
we use zeroMQ to send the control commands 
This script runs at the remote driver end. 
Receives joystick messages and sends it over the socket 
"""

event_handler={
    'wheel':wheel_callback,
    'joystick':js_callback
}

driver_config = toml.load(os.environ['DEVICE_CONFIG'])
device_config = driver_config['peripheral']
device = device_config.get('device','joystick') #default = joystick
heartbeat_freq = device_config.get('sampling_time',0.5)
test_stub = pd.read_csv(os.environ["CONFIG_PATH"] / Path("test_joystick.csv"))

def publish_check(last_activity_time, last_command_time):
    if time.time() - last_command_time > 1.0:
        return True, "control"
    elapsed_time = time.time() - last_activity_time
    if elapsed_time > heartbeat_freq:
        return True, "heartbeat"
    return False, None

def publish_control(sock, packet_id, command):
    sock.publish("controller", Schema.ControlMessage(
                                 time=time.time(),
                                 packet_id=packet_id,
                                 commands=command.keys(),
                                 values=map(int,command.values())))

def publish_heartbeat(sock):
    sock.publish("heartbeat", Schema.Heartbeat())

def talker():
    server_sync = Sync()
    server_sync.receive_handshake()
    sock = Bus(subscribe=False)
    remote_driver = RemoteDrive()
    last_activity_time = time.time()
    packet_id = 0
    last_command_time = time.time()
    while True:
        publish_flag, message = publish_check(last_activity_time, last_command_time)  
        if publish_flag:
            if message == "control":
                cmd = test_stub.loc[packet_id].to_dict() 
                print(cmd)
                publish_control(sock,packet_id,cmd)
                packet_id += 1
                last_command_time = time.time()
            else:
                publish_heartbeat(sock)
            last_activity_time = time.time()


if __name__ == '__main__':
    talker()

