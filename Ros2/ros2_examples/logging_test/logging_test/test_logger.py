#!/usr/bin/env python3

import rclpy
from .get_logger import get_logger
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node('logtest')
    node.get_logger().info('test logger')

    logger = get_logger('info_logger', 'info')
    logger.info('info logger')
    
    # get logger from a helper function and check the severity level
    warn_logger = get_logger('warn_logger', 'warn')
    level = rclpy.logging.get_logger_effective_level(warn_logger.name) 
    warn_logger.log('warn logger', level)
    assert level == rclpy.logging.LoggingSeverity.WARN
    
    debug_logger = get_logger('debug_logger', 'debug')
    level = rclpy.logging.get_logger_effective_level(debug_logger.name) 
    debug_logger.log('debug logger', level)
    assert level == rclpy.logging.LoggingSeverity.DEBUG
    
    #try to get a logger for a non existent severity level, will return a logger with info level
    non_existent_level = get_logger('debug33_logger', 'debug33')
    non_existent_level.info('nonexistent level')
    print('debug33 logger level:', rclpy.logging.get_logger_effective_level(non_existent_level.name))

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == '__main__':
    main()
