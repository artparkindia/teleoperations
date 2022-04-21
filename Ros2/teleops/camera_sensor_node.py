import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from rclpy.qos import QoSProfile
from rclpy.duration import Duration
from rclpy.qos_event import PublisherEventCallbacks

import numpy as np
import threading
import cv_bridge
import cv2
import time

class CameraSensor(Node):
    def __init__(self):
        super().__init__('camera_sensor')
        qos_profile = QoSProfile(
            depth=10,
            deadline=Duration(seconds=5))
        publisher_callbacks = PublisherEventCallbacks(
            deadline=lambda event: self.get_logger().info(f'Deadline missed {event.total_count} times'))
        self.pub = self.create_publisher(Image, 'camerasensor', qos_profile,
                                         event_callbacks=publisher_callbacks)
        self.cap = cv2.VideoCapture('/home/siddhya/Downloads/SampleVideo_1280x720_5mb.mp4')
        if not self.cap.isOpened():
            print("Error opening resource: ")
        else:
            threading.Thread(target=self.wait_for_frame).start()

    def wait_for_frame(self):
        bridge = cv_bridge.CvBridge()
        while True:
            rval, frame = self.cap.read()
            if not rval:
                break
            if frame is None:
                print("was none")
                continue
            msg = bridge.cv2_to_imgmsg(frame, encoding='passthrough')
            self.get_logger().info('Publishing')
            self.pub.publish(msg)
            time.sleep(1)


def main():
    rclpy.init()
    node = CameraSensor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
