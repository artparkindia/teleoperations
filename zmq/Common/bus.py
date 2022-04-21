import zmq
import os
import sys
import toml
import Schema
import logging
import itertools


network_config = toml.load(os.environ["DEVICE_CONFIG"]).get('network')
REMOTE_IP = network_config['remote_ip']
REMOTE_PORT = network_config['msg_port']
SYNC_PORT = network_config['sync_port']
NETWORK_TIMEOUT = network_config.get('timeout',-1)
REQUEST_RETRIES = 3
REQUEST_TIMEOUT = 3000

class Bus(object):
    def __init__(self, subscribe, local=False):
        context = zmq.Context()
        self.subscribe_flag = subscribe 
        if subscribe:
            self.sub = context.socket(zmq.SUB)
            if local:
                self.sub.connect(f"tcp://0.0.0.0:{REMOTE_PORT}")
            else:
                self.sub.connect(f"tcp://{REMOTE_IP}:{REMOTE_PORT}")
            if NETWORK_TIMEOUT > 0:
                self.sub.setsockopt(zmq.RCVTIMEO, NETWORK_TIMEOUT)     
                self.sub.setsockopt_string(zmq.SUBSCRIBE, "heartbeat")
        else:
           self.pub = context.socket(zmq.PUB)
           self.pub.bind(f"tcp://0.0.0.0:{REMOTE_PORT}")

    def subscribe(self, topic):
        self.sub.setsockopt_string(zmq.SUBSCRIBE, topic)

    def publish(self, topic, message):
        return self.pub.send(Schema.encode_message(topic, message))

    def receive(self):
        return Schema.decode_message(self.sub.recv())

    def close(self):
        if self.subscribe_flag:
            self.sub.close()
        else:
            self.pub.close()

#  Lazy Pirate server-client
#   Author: Daniel Lundin <dln(at)eintr(dot)org>
class Sync(object):
    def __init__(self, client=False):
        self.context = zmq.Context()
        if client:
            self.peer_endpoint = f"tcp://{REMOTE_IP}:{SYNC_PORT}"
            self.client= self.context.socket(zmq.REQ)
            self.client.connect(self.peer_endpoint)
        else:
            self.peer_endpoint = f"tcp://*:{SYNC_PORT}"
            self.server = self.context.socket(zmq.REP)
            self.server.bind(self.peer_endpoint)

    def initiate_handshake(self):
        for sequence in itertools.count():
            request = str(sequence).encode()
            print(f"Sending {request}")
            self.client.send(request)
            retries_left = REQUEST_RETRIES
            while True:
                if (self.client.poll(REQUEST_TIMEOUT) & zmq.POLLIN) != 0:
                    reply = self.client.recv()
                    print(f"reply {reply}")
                    if int(reply) == sequence:
                        print(f"Server replied OK {reply}")
                        print("Handshake complete")
                        retries_left = REQUEST_RETRIES
                        return 
                    else:
                        logging.error(f"Malformed reply from server: {reply}")
                        continue
                retries_left -= 1
                logging.warning("No response from server")
                # Socket is confused. Close and remove it.
                self.client.setsockopt(zmq.LINGER, 0)
                self.client.close()
                if retries_left == 0:
                    logging.error("Server seems to be offline, abandoning")
                    sys.exit()
                print("Reconnecting to server…")
                # Create new connection
                self.client = self.context.socket(zmq.REQ)
                self.client.connect(self.peer_endpoint)
                print(f"Resending {request}")
                self.client.send(request)

    def receive_handshake(self):
        while True:
            request = self.server.recv()
            print(f"Received from client {request}")
            self.server.send(request)
            print("Handshake complete")
            break
        self.server.close()

