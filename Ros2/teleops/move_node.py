import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Empty
from rcl_interfaces.msg import SetParametersResult
import time
import serial
import json
import os
import toml

dirname = os.path.dirname(__file__)
config_file = os.path.join(dirname, 'config.toml')
heartbeat_config = toml.load(config_file)['heartbeat']

class Move(Node):
    def __init__(self):
        super().__init__('move')
        self.declare_parameter('serial_port', '/dev/ttyACM0')
        self.declare_parameter('baud_rate', '115200')
        self.add_on_set_parameters_callback(self.params_cb)
        self.sub = self.create_subscription(
            String, 'move', self.callback, 3)
        self.create_subscription(String, 'heartbeat', self.callback_heartbeat, 0)

        try:
            self.port = serial.Serial(self.get_parameter('serial_port').get_parameter_value().string_value,
                                      self.get_parameter('baud_rate').get_parameter_value().string_value)
        except serial.SerialException:
            self.get_logger().info(f'Cound not open serial port')
            self.port = None
        self.srv = self.create_service(Empty, f'{self.get_name()}/watchdog', lambda _, response: response)

        self.last_heartbeat_time = time.time()
        self.emergency_brake_commands = heartbeat_config['emergency_commands']
        self.heartbeat_interval = heartbeat_config['heartbeat_interval']
        self.heartbeat_timedout = False
        self.create_timer(self.heartbeat_interval, self.heartbeat_check)

    def params_cb(self, params):
        self.port = serial.Serial(self.get_parameter('serial_port').get_parameter_value().string_value,
                                  self.get_parameter('baud_rate').get_parameter_value().string_value)
        return SetParametersResult(successful=True)

    def callback_heartbeat(self, target):
        self.last_heartbeat_time = time.time()
        self.heartbeat_timedout = False

    def callback(self, msg=None, emergency = False):
        data = json.loads(msg.data)['commands'] if not emergency else self.emergency_brake_commands
        if len(data) > 0:
            if self.port:
                for command in data:
                    message = command.encode('utf-8')
                    self.get_logger().info('command to be sent:', message)
                    self.port.write(message)
            else:print('no serial interface found, command recieved:', *data)

    def heartbeat_check(self):
        if not self.heartbeat_timedout and (time.time()-self.last_heartbeat_time > self.heartbeat_interval):
            self.callback(emergency=True)           
            self.get_logger().warn(f'heartbeat timeout, data sent: {self.emergency_brake_commands}')
            self.heartbeat_timedout = True

def main():
    rclpy.init()
    node = Move()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt as e:
        node.get_logger().warn(f"Keyboard interrupt")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()