import os
import toml
import subprocess

video_config = toml.load(os.environ["COMMON_CONFIG"])['video']
UDP_PORT = video_config['udp_port'] 

play_command = ["ffplay", f"udp://127.0.0.1:{UDP_PORT}","-loglevel","quiet"]
subprocess.call(play_command)
