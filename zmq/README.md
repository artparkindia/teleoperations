### ZeroMQ for teledriving

- User has to execute two files ``` robot.service ``` and ``` teleoperator.service ``` 
- Add the remote ip-address in `Configs/robot_config.toml` 
- In the above file set the `testing` parameter as needed to True/False
- Connecting the joystick user can send the commands to the robot where the joystick values are mapped to robot commands in `Configs/generate_driver_settings` and `Configs/generate_robot_settings`
- In Onboard_Vehicle folder you can find the `move_vehicle` file that sends the commands to the robot and `motor_controller` that maps the joystick values to commands.
- In Remote_Driver folder you can find `teleoperator` file that receives commands from Joystick. `controller` file maps the joystick continuous values to discrete values which is inturn mapped to robot commands on Onboard_Vehicle as specified in `robot_settings.json` 