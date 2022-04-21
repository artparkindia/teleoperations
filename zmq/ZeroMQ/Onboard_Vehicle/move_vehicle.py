import os
import json
import toml
from pathlib import Path
from Common.bus import Bus, Sync
from Onboard_Vehicle.motor_controller import MotorController
"""
In this test code we are testing basic vehicle control over the network
we use zeroMQ  to send the control commands 
This script runs at the onboard vehicle end. 
Receives joystick messages after opening a socket
then writes the command to serial interface in the callback function
"""

robot_config = toml.load(os.environ["DEVICE_CONFIG"])
testing = robot_config["testing"]

def listener():
    motor_controller = MotorController(testing)
    sync_client = Sync(client=True)
    sync_client.initiate_handshake()
    sock = Bus(subscribe=True)
    sock.subscribe("controller")
    while True:
        try:
            topic, command = sock.receive()
        except Exception:
            print("Network timeout.. stopping vehicle")
            motor_controller.callback(None)
            break
        if topic == "controller":
            motor_controller.callback(command)
    sock.close()

if __name__ == '__main__':
    listener()
