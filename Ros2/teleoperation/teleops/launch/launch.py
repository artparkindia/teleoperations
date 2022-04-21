from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('teleops'),
        'params.yaml'
        )

    return LaunchDescription([
        Node(
            package='teleops',
            executable='joystick_sensor_node',
            parameters=[config],
        ),
        Node(
            package='teleops',
            executable='move_node',
            parameters=[config],
        ),
        Node(
            package='teleops',
            executable='vehicle_controller_node',
            parameters=[config],
        ),
    ])