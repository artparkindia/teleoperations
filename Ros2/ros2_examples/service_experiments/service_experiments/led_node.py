# !/usr/bin/env python3

import rclpy
from led_interface.msg import LedState
from led_interface.srv import SetLed
from rclpy.node import Node

class LedPanel(Node):

	def __init__(self):
		super().__init__('led_node')
		self.declare_parameter("led_state",[0,0,0])
		self.create_service(SetLed,'set_led',self.callback_set_led)
		self.publisher = self.create_publisher(LedState,'led_state',10)
		self.create_timer(1,self.publish_led_state)
		self.led_state = self.get_parameter("led_state").value
		self.get_logger().info('Led panel initialized')

	def callback_set_led(self,request,response):
		led_number = request.led_number
		led_state = request.state
		if led_number <= 0 or led_number >3:
				response.success = False
				return response
		self.led_state[led_number-1] = int(led_state)
		self.publish_led_state()
		response.success = True

		return response
	
	def publish_led_state(self):
		led_state = LedState()
		led_state.state = self.led_state
		self.publisher.publish(led_state)
		self.get_logger().info(','.join(map(str, self.led_state)))

def main(args=None):
	rclpy.init(args=args)
	node = LedPanel()
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	node.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
		main()
