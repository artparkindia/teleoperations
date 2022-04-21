import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Empty
from rcl_interfaces.msg import SetParametersResult
from .remote_drive import RemoteDrive
from .kuka_drive import KukaDrive
import pygame
import json
import toml
import os


class KeyboardMap:
    def __init__(self) -> None:
        self.actions = {
            'f': '0002' + 'FORWA@',
            'n': '0002' + 'NEUTR@',
            'r': '0002' + 'REVER@',
            '\x1b[A': '0016' + '#0120T@',
            '\x1b[B': '0001' + '#0260B@',
            '\x1b[C': '0017' + '#2000S@',  # left
            '\x1b[D': '0017' + '#1000S@',  # right
        }

    def get_cmd(self, msg):
        return self.actions.get(msg, '')

class KukaMap(KukaDrive):
    def __init__(self):
        super().__init__()
        
    def get_cmd(self, msg):
        event = json.loads(msg)
        if event['type'] == pygame.JOYAXISMOTION:
            self.axis_val = event['value']
            self.update_axis_arm(self.axis_val, event['axis'])

        elif event['type'] == pygame.JOYBUTTONDOWN:
            self.button = event['button']
            self.update_button_arm(self.button)

        elif event['type'] == pygame.JOYBUTTONUP:
            self.reset_command() 
        
        control_cmd = self.get_commands()
        return control_cmd 

class JoystickMap(RemoteDrive):

    def __init__(self):
        super().__init__()
        self.axis_val=None
        self.button=None
        self.prev_cmd = (0, 0, 0, 0)
        self.PREV_CMD_IDX = 0
        self.NEW_CMD_IDX = 1

    def command_xor(self, control_cmd):
        return list(filter(lambda x:x[self.PREV_CMD_IDX] != x[self.NEW_CMD_IDX], zip(self.prev_cmd, control_cmd)))

    def get_cmd(self, msg):
        event = json.loads(msg)
        if event['type'] == pygame.JOYAXISMOTION and event['axis'] == 1:
            self.axis_val = event['value']
            if not self.emergency:self.update_brake_throttle(self.axis_val)

        elif event['type'] == pygame.JOYBUTTONDOWN:
            self.button = event['button']
            self.update_brake_gear(self.button, self.axis_val)

        elif event['type'] == pygame.JOYBUTTONUP:
            self.reset_steer()

        control_cmd = self.get_commands()
        compare_res = self.command_xor(control_cmd)
        command_array = []

        if len(compare_res) > 0 : 
            self.prev_cmd = control_cmd
            for cmd in compare_res:
                command_array.append(cmd[self.NEW_CMD_IDX])
        return command_array

class VehicleController(Node):
    
    def __init__(self):
        super().__init__('vehicle_controller')
        self.declare_parameter('input', 'joystick')
        self.add_on_set_parameters_callback(self.params_cb)
        self.params_cb(None)      
        self.pub = self.create_publisher(String, 'move',3)
        self.srv = self.create_service(Empty, f'{self.get_name()}/watchdog', lambda _, response: response)

    def params_cb(self, params):
        input_device = self.get_parameter('input').get_parameter_value().string_value
        if input_device == 'joystick':
            input_channel = 'joysticksensor'
            self.map = JoystickMap()
        elif input_device == 'keyboard':
            input_channel = 'keysensor'
            self.map = KeyboardMap()
        elif  input_device == 'joystick_kuka':
            input_channel = 'joysticksensor'
            self.map = KukaMap()
        else:
            self.get_logger().info('Could not find the specified map')

        self.sub = self.create_subscription(
            String, input_channel, self.callback, 3)
        return SetParametersResult(successful=True)

    def callback(self, msg):
        self.get_logger().info('Received: "%r"' % msg.data)
        cmd = String()
        command_list = self.map.get_cmd(msg.data)
        if(len(command_list)>0):
            cmd.data = json.dumps({
                'commands':command_list
            })
            self.get_logger().info('Publishing: "%s"' % cmd.data)
            self.pub.publish(cmd)


def main():
    rclpy.init()
    node = VehicleController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt as e:
        node.get_logger().warn(f'Keyboard interrupt')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()