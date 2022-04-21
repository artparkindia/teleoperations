import rclpy
from rclpy.node import Node
from teleops_interfaces.msg import Latency
from rcl_interfaces.msg import SetParametersResult
import socket

class LatencyCheck(Node):
    def __init__(self):
        super().__init__('latency_check')
        self.name = socket.gethostname()
        self.declare_parameter('hostname', self.name)
        self.add_on_set_parameters_callback(self.params_cb)
        self.pub = self.create_publisher(Latency, 'latency', 3)
        self.sub = self.create_subscription(Latency, 'latency', self.callback, 3)
        self.create_timer(1, self.timer_cb)
        self.count = 0

    def params_cb(self, params):
        self.name = self.get_parameter('hostname')
        return SetParametersResult(successful=True)

    def timer_cb(self):
        msg = Latency()
        msg.seq = self.count
        self.count += 1
        msg.src_id = self.name
        msg.src_ts = self.get_clock().now().nanoseconds
        #self.get_logger().info(f'Publishing: seq {msg.seq} src_id {msg.src_id} src_ts {msg.src_ts}')
        self.pub.publish(msg)

    def callback(self, msg):
        now = self.get_clock().now().nanoseconds
        #self.get_logger().info(f'Received: seq {msg.seq} src_id {msg.src_id} src_ts {msg.src_ts}')
        if msg.src_id == self.name:
            host = msg.dst_id if msg.dst_id else 'localhost'
            self.get_logger().info(f'Host: {host} Latency: {(now - msg.src_ts)/2000000}ms')
        elif not msg.dst_id:
            reply = Latency()
            reply.src_id = msg.src_id
            reply.src_ts = msg.src_ts
            reply.dst_id = self.name
            reply.dst_ts = self.get_clock().now().nanoseconds
            #self.get_logger().info(f'Publishing: seq {msg.seq} src_id {msg.src_id} src_ts {msg.src_ts}')
            self.pub.publish(reply)

def main():
    rclpy.init()
    node = LatencyCheck()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
