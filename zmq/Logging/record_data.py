import os
import csv
import toml
import click
import time
import logging
from datetime import datetime
from Common.bus import Bus, Sync
from Common.ntp_time_sync import synchronize

#time_correction = synchronize()
time_correction=0.0
print(f"NTP time correction {time_correction}s")
print("Ready to start operation")

def data_callback(writer, message):
    data = list([message.time,message.packet_id]) + list(message.values)
    writer.writerow([time.time()+time_correction]+data)

@click.command()
@click.option("--local/--remote", default=False)
def recorder(local):
    hostname = 'driver' if local else 'robot'
    sock = Bus(subscribe=True,local=local)
    sock.subscribe("controller")
    recorder_folder = toml.load(os.environ['COMMON_CONFIG'])['recorder']["record_path"]
    log_folder = "log_" + datetime.now().isoformat()
    location = f"{recorder_folder}/{log_folder}"
    os.mkdir(f"{location}")
    file_desc = open(f"{location}/controller_{hostname}.csv", "w", newline="")
    data_writer = csv.writer(file_desc)
    data_writer.writerow(["recv_time","time","id","steer","brake","throttle","gear"])
    while True:
        #hacky - need to fix zmq resource error
        try:
            topic, message = sock.receive()
        except:
            continue
        if topic == 'controller':
            data_callback(data_writer, message)

if __name__ == '__main__':
    recorder()
