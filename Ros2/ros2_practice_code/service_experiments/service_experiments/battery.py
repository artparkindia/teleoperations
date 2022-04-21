#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from led_interface.srv import SetLed
from functools import partial

class Battery(Node):
	
	def __init__(self):
		super().__init__('battery_node')
		self.client = self.create_client(SetLed,'set_led')
		self.declare_parameter('led_number',2)
		led_number = self.get_parameter('led_number').value
		self.battery_state = 1
		self.led_number = led_number
		self.count = 0
		self.create_timer(1,self.callback_battery_state)
		self.get_logger().info("Battery node initialized")

	def callback_battery_state(self):
		self.count = (self.count+1)%10
		self.get_logger().info(f"count:{self.count}")
		if self.count == 4:self.pass_led_state(self.led_number,1)
		elif self.count == 0:self.pass_led_state(self.led_number,0)
	
	def pass_led_state(self,led_number=2,state=0):
		
		while not self.client.wait_for_service(1):
				self.get_logger().info('waiting for set_led service ...')
	
		request = SetLed.Request()
		request.led_number = led_number
		request.state = bool(state)

		future = self.client.call_async(request)
		future.add_done_callback(partial(self.callback_set_led_service_response,number=led_number,state=state))

	def callback_set_led_service_response(self,future,number,state):
		try:
			response = future.result()
			self.get_logger().info(f'result of setting led {number} to state {state} is {response.success}')
		except Exception as e:
			self.get_logger().error('error in service response {e}')
	

def main(args = None):
	rclpy.init(args=args)
	node = Battery()
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	node.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
		main()
