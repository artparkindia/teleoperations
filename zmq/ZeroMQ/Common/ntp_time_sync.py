import time
import ntplib
import logging
import numpy as np

max_tries = 5 
num_samples = 5 

def synchronize():
    ntpc = ntplib.NTPClient()
    server = '0.in.pool.ntp.org'
    response = None
    iterations = 1
    arr = []
    while len(arr) < num_samples-1:
        try:
            for _ in range(num_samples-len(arr)):
                response = ntpc.request(server, version=3)
                arr.append(response.orig_time - time.time())
        except:
            iterations += 1
            logging.info(f"iter:{iterations} samples{len(arr)}: sync again")
            if iterations > max_tries:
                if arr:
                    return np.mean(arr)
                else:
                    logging.info("Unable to NTP sync. No corrections applied")
                    return 0.0 
    return np.mean(arr)   

if __name__ == "__main__":
    delay = sync_system_time()
    logging.info(delay)
