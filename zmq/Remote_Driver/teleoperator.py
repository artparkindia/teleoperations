import sys
import os
import pygame
import time
import toml
import Schema
import numpy as np

from pathlib import Path
from Common.bus import Bus, Sync
from Remote_Driver.callbacks import event_handler 
from Remote_Driver.controller import RemoteDrive

"""
In this test code we are testing basic vehicle control over the network
we use zeroMQ to send the control commands 
This script runs at the remote driver end. 
Receives joystick messages and sends it over the socket 
"""

driver_config = toml.load(os.environ['DEVICE_CONFIG'])
device_config = driver_config['peripheral']
DEVICE = device_config.get('device','joystick') #default = joystick
HEARTBEAT_FREQ = device_config.get('sampling_time',0.2)

def publish_check(events, remote_driver, elapsed_time):
    if remote_driver.emergency or len(events)>0:
        return True, "control"
    if elapsed_time > HEARTBEAT_FREQ:
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

def initialize():
    pygame.init()
    pygame.joystick.init()
    handler = pygame.joystick.Joystick(0)
    handler.init()
    return handler

def talker():
    handler = initialize()
    sync_server = Sync()
    sync_server.receive_handshake()
    sock = Bus(subscribe=False)
    remote_driver = RemoteDrive()
    last_activity_time = time.time()
    packet_id = 0
    while True:
        events = pygame.event.get()
        event_handler[DEVICE](remote_driver, handler, events)
        elapsed_time = time.time() - last_activity_time
        publish_flag, message = publish_check(events,remote_driver, elapsed_time)  
        if publish_flag:
            if message == "control":
                cmd = remote_driver.get_commands()
                print(cmd)
                publish_control(sock,packet_id,cmd)
                packet_id += 1
            else:
                publish_heartbeat(sock)
            last_activity_time = time.time()


if __name__ == '__main__':
    talker()

