import toml
import json
import time
import os

dirname = os.path.dirname(__file__)
config_filename = os.path.join(dirname, 'config_remote.toml')
config_data =  toml.load(config_filename)
button_map = config_data['button_map_kuka']


class KukaDrive(object):
    def __init__(self):
       self.move = []
    
    def update_axis_arm(self, command, event_axis=1):
        if event_axis == 1:
            if command > 0:
                self.move = ["down"]

            elif command <= 0:
                self.move = ["up"]
        elif event_axis == 0:
            if command > 1e-3:
                self.move = ["right"]

            elif command < 1e-3:
                self.move = ["left"]

    def update_button_arm(self, button):

        if button == button_map['up']:
            self.move = ["up"]
        
        elif button == button_map['down']:
            self.move = ["down"]

        elif button == button_map['left']:
            self.move = ["left"]
    
        elif button == button_map['right']:
            self.move = ["right"]
    
    def reset_command(self):
        self.move = []

    def get_commands(self):        
        return self.move
       


            
