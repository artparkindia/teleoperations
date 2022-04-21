import os
import glob
import numpy as np
import pandas as pd

recorder_folder = './data'
sub_dirs = os.listdir(recorder_folder)
full_dir = [os.path.join(recorder_folder, s) for s  in sub_dirs]
full_dir.sort(key=lambda x:os.path.getmtime(x))
last_run = full_dir[-1]
data = glob.glob(last_run+"/*.csv")[0]
log_data = pd.read_csv(data)
delay = np.array(log_data['recv_time'] - log_data['time'])
print(f"Total packets received = {log_data.shape[0]}")
print(f"Packets lost = {np.sum(np.diff(log_data['id']) > 1)}")
print(f"Average Packet delay = {np.mean(delay)*1000:0.3} ms")
print(f"Packet jitter = {np.std(delay)*1000:0.3} ms")
