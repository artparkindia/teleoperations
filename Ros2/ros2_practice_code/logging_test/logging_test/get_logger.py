#!/usr/bin/env python3 

import rclpy
from rclpy.logging import LoggingSeverity 


def get_logger(name='name', severity='info'):
    
        severity_levels = {
            'debug':LoggingSeverity.DEBUG,
            'info':LoggingSeverity.INFO,
            'warn':LoggingSeverity.WARN,
            'error':LoggingSeverity.ERROR,
            'fatal':LoggingSeverity.FATAL
        }
    
        if name!='' and severity.lower() in severity_levels:
            logger = rclpy.logging.get_logger(name)
            logger.set_level(severity_levels[severity])
        else:
            logger = rclpy.logging.get_logger('default info logger')

        return logger
