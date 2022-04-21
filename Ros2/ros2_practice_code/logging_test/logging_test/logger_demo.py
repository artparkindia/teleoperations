#!/usr/bin/env python3

import os
import rclpy
from rclpy.logging import LoggingSeverity
from rclpy.node import Node

class Logger(Node):
    def __init__(self):
        
        super().__init__('logger')
        self.get_logger().info("logger node init")
       
        # create loggers : debug, info(default),warn, error and fatal
        # name of the logger self.get_logger() is 'logger'

        debug_logger_name = 'debug_logger'
        default_logger_name = 'info_logger'
        warn_logger_name = 'warn_logger' 
        error_logger_name = 'error_logger'
        fatal_logger_name = 'fatal_logger'

        # get loggers
        self.debug_logger = rclpy.logging.get_logger(debug_logger_name)
        self.default_logger = rclpy.logging.get_logger(default_logger_name)
        self.warn_logger = rclpy.logging.get_logger(warn_logger_name)
        self.error_logger = rclpy.logging.get_logger(error_logger_name)
        self.fatal_logger = rclpy.logging.get_logger(fatal_logger_name)

        # set logger severity levels
        # not setting the severity level for default(info) logger
        rclpy.logging.set_logger_level('debug_logger', LoggingSeverity.DEBUG)
        rclpy.logging.set_logger_level('warn_logger', LoggingSeverity.WARN)
        rclpy.logging.set_logger_level('error_logger', LoggingSeverity.ERROR)
        rclpy.logging.set_logger_level('fatal_logger', LoggingSeverity.FATAL)
        
        # check the severity levels
        # these messages will be logged with the name of the logger 'logger'
        self.get_logger().info(f"debug logger severity {rclpy.logging.get_logger_effective_level(debug_logger_name)}")
        self.get_logger().info(f"root logger severity {rclpy.logging._root_logger.get_effective_level()}")
        self.get_logger().info(f"default(info) logger severity {rclpy.logging.get_logger_effective_level(default_logger_name)}")
        self.get_logger().info(f"warn logger severity {rclpy.logging.get_logger_effective_level(warn_logger_name)}")
        self.get_logger().info(f"error logger severity {rclpy.logging.get_logger_effective_level(error_logger_name)}")
        self.get_logger().info(f"fatal logger severity {rclpy.logging.get_logger_effective_level(fatal_logger_name)}")
        
        self.create_timer(1, self.callback_timer)
        self.count = 1

    def callback_timer(self):
        self.count += 1
        # check hierarchy of levels debug<info<warn<error<fatal
        # a logger set to a level only logs messages with severity >= the set level of the logger

        # logs messages with the corresponding logger name
        self.debug_logger.debug(f"debug count:{self.count}")
        self.default_logger.info(f"info count:{self.count}") 

        self.warn_logger.warn(f"warn count:{self.count}") 
        self.warn_logger.info(f"warn logger set to info count")#this will not be logged, used level info  < set level warn
        
        self.error_logger.error(f"error count:{self.count}") 
        self.error_logger.warn(f"error logger set to warn count")#this will not be logged, used level warn < set level error
        
        self.fatal_logger.fatal(f"fatal count:{self.count}") 
        self.fatal_logger.error(f"fatal logger set to error count")#this will not be logged, used level error < set level fatal

def main(args=None):
    #formatting the logger output
    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '[{severity} {time}][{name}]:{message} at {file_name} {line_number}'
    rclpy.init(args=args)
    node = Logger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # clear the logger formatting
        del os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT']
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    #default log location ~/.ros/log or logged to dir in env var ROS_LOG_DIR OR ROS_HOME/log
    main()
