from setuptools import setup

package_name = 'teleops'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/launch.py']),
        ('share/' + package_name, ['config/params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siddarth',
    maintainer_email='siddarth@artpark.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_sensor_node = teleops.keyboard_sensor_node:main',
            'joystick_sensor_node = teleops.joystick_sensor_node:main',
            'camera_sensor_node = teleops.camera_sensor_node:main',
            'vehicle_controller_node = teleops.vehicle_controller_node:main',
            'move_node = teleops.move_node:main',
            'latency_node = teleops.latency_node:main',
            'watchdog_node = teleops.watchdog_node:main',
        ],
    },
)
