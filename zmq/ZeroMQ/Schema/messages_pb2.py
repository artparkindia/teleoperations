# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='common.schema',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emessages.proto\x12\rcommon.schema\"S\n\x0e\x43ontrolMessage\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x11\n\tpacket_id\x18\x02 \x01(\r\x12\x10\n\x08\x63ommands\x18\x03 \x03(\t\x12\x0e\n\x06values\x18\x04 \x03(\r\"\x1e\n\tHeartbeat\x12\x11\n\tkeepalive\x18\x01 \x01(\tb\x06proto3'
)




_CONTROLMESSAGE = _descriptor.Descriptor(
  name='ControlMessage',
  full_name='common.schema.ControlMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='common.schema.ControlMessage.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packet_id', full_name='common.schema.ControlMessage.packet_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='common.schema.ControlMessage.commands', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='common.schema.ControlMessage.values', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=116,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='common.schema.Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive', full_name='common.schema.Heartbeat.keepalive', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['ControlMessage'] = _CONTROLMESSAGE
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlMessage = _reflection.GeneratedProtocolMessageType('ControlMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:common.schema.ControlMessage)
  })
_sym_db.RegisterMessage(ControlMessage)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:common.schema.Heartbeat)
  })
_sym_db.RegisterMessage(Heartbeat)


# @@protoc_insertion_point(module_scope)
