import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Empty
from rclpy.qos import QoSProfile
from rclpy.duration import Duration
from rclpy.qos_event import PublisherEventCallbacks

import threading
import getkey


class KeySensor(Node):
    def __init__(self):
        super().__init__('key_sensor')
        qos_profile = QoSProfile(
            depth=10,
            deadline=Duration(seconds=5))
        publisher_callbacks = PublisherEventCallbacks(
            deadline=lambda event: self.get_logger().info(f'Deadline missed {event.total_count} times'))
        self.pub = self.create_publisher(String, 'keysensor', qos_profile,
                                         event_callbacks=publisher_callbacks)
        self.srv = self.create_service(Empty, f'{self.get_name()}/watchdog', lambda _, response: response)

    def wait_for_key(self):
        msg = String()
        self.get_logger().info('Press "q" to quit')
        while True:
            msg.data = getkey.getkey()
            if msg.data == 'q':
                self.get_logger().info('Quiting')
                return
            self.get_logger().info('Publishing: "%r"' % msg.data)
            self.pub.publish(msg)


def main():
    rclpy.init()
    node = KeySensor()
    threading.Thread(target=rclpy.spin, args=(node,)).start()
    node.wait_for_key()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
