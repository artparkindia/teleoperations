#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):
	
	def __init__(self):
		super().__init__('number_counter')
		self.subsrciber = self.create_subscription(Int64,'number',self.count_handler,10)
		self.count = 0
		self.publisher = self.create_publisher(Int64,'number_count',10)
		self.clear_service = self.create_service(SetBool,'reset_counter',self.callback_reset_counter)
		self.get_logger().info("number counter initialized")
	
	def count_handler(self,msg):
		num_count = Int64()
		self.count += msg.data
		num_count.data = self.count
		self.publisher.publish(num_count)
	
	def callback_reset_counter(self, msg, response):

		if msg.data == True: 
			self.count = 0
			response.success = bool(1) #res_bool
			response.message = "Counter reset"
		else:
			response.success = bool(0)
			response.message = "counter state retained"

		return response
		

def main(args = None):
	rclpy.init(args=args)
	num_count = NumberCounter()
	rclpy.spin(num_count)
	rclpy.shutdown()

if __name__ == '__main__':
		main()
