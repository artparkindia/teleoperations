import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Empty
from rclpy.qos import QoSProfile
from rclpy.duration import Duration
from rclpy.qos_event import PublisherEventCallbacks

import threading
import pygame
import json
import time

class JoystickSensor(Node):
    def __init__(self):
        super().__init__('joystick_sensor')
        qos_profile = QoSProfile(
            depth=10,
            deadline=Duration(seconds=5))
        
        self.last_activity_time = time.time()
        self.pub = self.create_publisher(String, 'joysticksensor', 3)
        self.srv = self.create_service(Empty, f'{self.get_name()}/watchdog', lambda _, response: response)
        self.HEARBEAT_PUB_INTERVAL = 3
        self.heartbeat_pub  = self.create_publisher(String, "heartbeat", 0)
        self.create_timer(self.HEARBEAT_PUB_INTERVAL, self.heartbeat_callback)

        pygame.init()
        pygame.display.init()
        pygame.joystick.init()
        try:
            self.handler = pygame.joystick.Joystick(0)
            self.handler.init()
        except pygame.error as msg:
            self.get_logger().info(f'Could not open joystick device: {msg}')

    def prepare_data(self, data):
        pub_data = String()
        pub_data.data = data
        return pub_data

    def heartbeat_callback(self):
        self.heartbeat_pub.publish(self.prepare_data('pulse'))
        self.last_activity_time = time.time()

    def wait_for_input(self):
        msg = String()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.JOYAXISMOTION:
                msg.data = json.dumps({'type': event.type,
                                       'axis': event.axis,
                                       'value': event.value,
                                    })
            elif event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYBUTTONDOWN:
                msg.data = json.dumps({'type': event.type,
                                       'button': event.button
                                    })
            else:continue
            self.get_logger().info('Publishing: "%r"' % msg.data)
            self.pub.publish(msg)


def main():
    rclpy.init()
    node = JoystickSensor()
    try:
        threading.Thread(target=rclpy.spin, args=(node,)).start()
        node.wait_for_input()
    except KeyboardInterrupt as e:
        node.get_logger().warn(f"Keyboard interrupt")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
