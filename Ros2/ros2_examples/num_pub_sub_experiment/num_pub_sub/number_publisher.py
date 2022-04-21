#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisher(Node):
	def __init__(self, name='number_publisher'):
		super().__init__(name)
		self.publisher = self.create_publisher(Int64,'number',10)
		self.declare_parameter('number_to_publish',2)
		self.declare_parameter('publish_frequency',1)
		self.number = self.get_parameter('number_to_publish').value
		self.freq = self.get_parameter('publish_frequency').value
		self.get_logger().info("starting number publisher")
		self.create_timer(1/self.freq,self.NumPub)
		#self.get_logger().info(f"rclpy ok:{rclpy.ok()}")

	def NumPub(self):
		number = Int64()
		number.data = self.number
		self.publisher.publish(number)
		self.get_logger().info(f"number:{self.number}")

def main(args=None):
	rclpy.init(args=args)
	num_pub = NumberPublisher('num_pub')
	try:
		rclpy.spin(num_pub)
	except KeyboardInterrupt:
		pass	

	rclpy.shutdown()

if __name__=='__main__':
		main()
