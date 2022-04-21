from typing import Set
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_srvs.srv import Empty
from rcl_interfaces.msg import SetParametersResult
from functools import partial
from std_msgs.msg import String
import numpy as np
import time
import toml
import os 

dirname = os.path.dirname(__file__)
config_file = os.path.join(dirname, 'config.toml')
heartbeat_config = toml.load(config_file)['heartbeat']

class WatchDog(Node):
    def __init__(self):
        super().__init__('watchdog')
        self.declare_parameter('nodes', [])
        self.add_on_set_parameters_callback(self.param_cb)
        self.nodes = self.get_parameter('nodes').value
        # self.nodes.append('key_sensor')
        self.nodes.append('vehicle_controller')
        self.nodes.append('joystick_sensor')
        self.nodes.append('move')
        self.update_clients()
        self.create_timer(1, self.send_requests)
        self.create_subscription(String, 'heartbeat', self.callback_heartbeat, 0)
        self.last_heartbeat_time = time.time()
        self.heartbeat_timedout = False
        self.heartbeat_interval = heartbeat_config['heartbeat_interval']
        self.create_timer(self.heartbeat_interval, self.heartbeat_check)

    def param_cb(self, params):
        for param in params:
            if param.name == 'nodes' and param.type_ == Parameter.Type.STRING_ARRAY:
                self.nodes = list(set(self.nodes) | set(param.value))
                self.update_clients()
                return SetParametersResult(successful=True)
        return SetParametersResult(successful=False)

    def heartbeat_check(self):
        if not self.heartbeat_timedout and (time.time()-self.last_heartbeat_time > self.heartbeat_interval):            
            # self.get_logger().info('\033[91m'+f'heartbeat timeout'+'\033[0m')
            self.heartbeat_timedout = True
        if self.heartbeat_timedout:self.get_logger().warn('heartbeat timeout')

    def callback_heartbeat(self, target):
        self.last_heartbeat_time = time.time()
        self.heartbeat_timedout = False

    def update_clients(self):
        self.wd_clients = {}
        self.nodes_latency = {}
        self.ts = {}
        self.end_ts = {}
        for node in self.nodes:
            self.wd_clients[node] = self.create_client(
                Empty, f'/{node}/watchdog')
            self.nodes_latency[node] = []
            self.end_ts[node] = None

    def send_requests(self):
        for node in self.nodes:
            if self.end_ts[node] is None:
                self.get_logger().info(
                    '\033[91m' + f'Node: {node:20} No response\n' + '\033[0m')
            else:
                latency = (self.end_ts[node] - self.ts[node])/2000000
                self.get_logger().info(
                    f'Node: {node:20} Latency: {latency:4.2}ms\n')
                self.nodes_latency[node].append(latency)
                self.get_logger().info(f'Node: {node:20} Avg latency for last 100 packets : {sum(self.nodes_latency[node])/len(self.nodes_latency[node]):4.2}ms')
                self.get_logger().info(f'Node: {node:20} Packet jitter {np.std(self.nodes_latency[node]):4.2}ms')
                if(len(self.nodes_latency[node])>100):self.nodes_latency[node] = [] #latency values for last 100pings
            req = Empty.Request()
            self.wd_clients[node].call_async(
                req).add_done_callback(partial(self.done_cb, node))
            self.ts[node] = self.get_clock().now().nanoseconds
            self.end_ts[node] = None
        self.get_logger().info('\r' + ' ' * 60 +
                               '\033[F' * (len(self.nodes) + 1))

    def done_cb(self, node, _):
        self.end_ts[node] = self.get_clock().now().nanoseconds


def main():
    rclpy.init()
    node = WatchDog()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt as e:
        node.get_logger().info(f'Keyboard interrupt')
    node.destroy_node
    rclpy.shutdown()


if __name__ == '__main__':
    main()
