from Schema.messages_pb2 import *

TOPIC_MAPPING = {
    "controller": ControlMessage,
    "heartbeat": Heartbeat
}

class InvalidTopic(Exception):
    pass

class InvalidMessage(Exception):
    pass

def encode_message(topic, message):
    return bytes(topic, "utf-8") + b"\000" + message.SerializeToString()

def decode_message(packet):
    if b"\000" not in packet:
        raise InvalidMessage()
    topic, raw_message = packet.split(b"\000", maxsplit=1)
    topic = topic.decode("utf-8")
    if topic in TOPIC_MAPPING:
        message = TOPIC_MAPPING[topic]()
    else:
        raise InvalidTopic()
    message.ParseFromString(raw_message)
    return topic, message
