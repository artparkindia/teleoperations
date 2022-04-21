from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    num_pub_node = Node(
        package = "num_pub_sub",
        executable = "num_pub"
    )
    num_sub_node = Node(
        package = "num_pub_sub",
        executable = "num_sub"
    )
    ld.add_action(num_pub_node)
    ld.add_action(num_sub_node)
    return ld
