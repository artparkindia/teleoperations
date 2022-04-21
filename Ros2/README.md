## Ros2 Teleoperations

This repo has configurable Ros2 nodes for teleoperations with two interfaces built-in: Joystick(PS-4 controller) and Keyboard operations. This code was tested with nodes being on the same network or on different networks connected via husarnet for cyclonedds. In cases where there is no need for NAT traversal a 'xml' profile file is provided.

### Architecture 
- There are 3 nodes for managing the communication - input node(eg in repo: joystick_sensor, keyboard_sensor node), controller node and move node that interfaces with the vehicle/robot
- A watchdog node for measuring packet latency and jitter

### Usage
<b>ref files:joystick_sensor_node, vehicle_controller_node, move_node, watchdog_node</b>
- Input node: User has to provide an input node on the lines of joystick_sensor_node and keyboard_sensor_node. 
    - Goal of this node is to receive the data from the input device and send the raw data to the controller node. Any data processing is done only in controller node. 
    - For HEARTBEAT, both, a QoS([Quality of Service](https://docs.ros.org/en/galactic/Concepts/About-Quality-of-Service-Settings.html)) profile is shown and also a manual implementation is provided in the above file.
    - In the Manual implementation of HEARTBEAT, a topic is created and publisher(eg:joystick_sensor_node) publishes periodically. A subscriber(eg: move_node) to the topic from another node will check if it receives heartbeat signal periodically. If heartbeat fails, set of emergency commands are sent to the robot.
    - User has to create a service to enable latency computation for the watchdog node. Template is given in joystick_sensor_node.
    - ``` 
        colcon build --packages-select teleops
        ros2 run teleops joystick_sensor_node
        ros2 run teleops vehicle_controller_node
        ros2 run teleops move_node --ros-args -p serial_port:=<port-id> -p baud_rate=<baudrate>
        ros2 run teleops watchdog_node  --ros-args -p nodes:=<[node1, node2]>
      ```
- Controller node: User has to define the mapping from the input commands received from the device to robot commands. Eg: JoystickMap, KeyboardMap is provided in the vehicle_controller_node
- Robot interface node: This sends out the commands to the robot whose port is defined in the command. Eg: move_node. This node also sends out the emergency commands if there is a failure of heartbeat. User has to pass the baud_rate and serial_port address.
- Watchdog node: Calculates the latency and packet jitter from self to the other nodes which are added in the watchdog node for monitoring

### Network
- All nodes on same network: No config changes needed.
- Nodes on different network: Connect via [Husarnet](https://husarion.com/tutorials/other-tutorials/husarnet-cyclone-dds/). If using <b>CycloneDDS, Check the network interface</b> in the cyclonedds.xml, it set to 'Auto' and if it does not pick up Husarnet virtual network interface <b>hnet0</b>, set it manually instead of 'Auto'.
- Nodes on different sub-domain: Add the ip-address in the cyclonedds/fastrtps xml file.  For installing and configuring Cyclone DDS refer [this](https://docs.ros.org/en/galactic/Installation/DDS-Implementations/Working-with-Eclipse-CycloneDDS.html), for Fast DDS refer [this](https://docs.ros.org/en/galactic/Installation/DDS-Implementations/Working-with-eProsima-Fast-DDS.html)