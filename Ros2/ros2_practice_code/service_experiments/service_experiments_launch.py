from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    battery_node = Node(
        package = 'service_experiments',
        executable = 'battery'
    )
    led_node = Node(
        package = 'service_experiments',
        executable = 'led'
    )
    ld.add_action(battery_node)
    ld.add_action(led_node)
    return ld
        
