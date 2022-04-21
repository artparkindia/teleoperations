import os
import toml
import subprocess

video_config = toml.load(os.environ["COMMON_CONFIG"])['video']
UDP_PORT = video_config['udp_port'] 
BITRATE = video_config['bitrate']
PRESET = video_config['preset']
ASPECT = video_config['aspect']
THREADS = video_config['threads']

device_config = toml.load(os.environ["DEVICE_CONFIG"])
VIDEO_SOURCE = device_config['video']['usb_port']
REMOTE_IP = device_config['network']['remote_ip']

video_command = ["ffmpeg", "-i", f"{VIDEO_SOURCE}", "-codec:v", "libx264", \
                 "-b:v", f"{BITRATE}", "-preset", f"{PRESET}", "-tune", \
                 "zerolatency", "-s", f"{ASPECT}","-threads",f"{THREADS}", \
                 "-f", "mpegts", f"udp:{REMOTE_IP}:{UDP_PORT}", \
                 "-analyzeduration","0","-probesize","32",\
                 "-loglevel", "quiet","-fflags","nobuffer"
                 ]
subprocess.call(video_command)
