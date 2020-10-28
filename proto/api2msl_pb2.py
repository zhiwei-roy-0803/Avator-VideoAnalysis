# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/api2msl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/api2msl.proto',
  package='api2visual',
  syntax='proto3',
  serialized_options=b'\n\030io.grpc.examples.api2mslB\010A2MProtoP\001\242\002\003A2M',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13proto/api2msl.proto\x12\napi2visual\"\x1c\n\rBundleRequest\x12\x0b\n\x03\x62uf\x18\x01 \x01(\x0c\"\x19\n\tJsonReply\x12\x0c\n\x04json\x18\x01 \x01(\t2H\n\x07\x41pi2Msl\x12=\n\x07GetJson\x12\x19.api2visual.BundleRequest\x1a\x15.api2visual.JsonReply\"\x00\x42,\n\x18io.grpc.examples.api2mslB\x08\x41\x32MProtoP\x01\xa2\x02\x03\x41\x32Mb\x06proto3'
)




_BUNDLEREQUEST = _descriptor.Descriptor(
  name='BundleRequest',
  full_name='api2visual.BundleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buf', full_name='api2visual.BundleRequest.buf', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=35,
  serialized_end=63,
)


_JSONREPLY = _descriptor.Descriptor(
  name='JsonReply',
  full_name='api2visual.JsonReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='api2visual.JsonReply.json', index=0,
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
  serialized_start=65,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['BundleRequest'] = _BUNDLEREQUEST
DESCRIPTOR.message_types_by_name['JsonReply'] = _JSONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BundleRequest = _reflection.GeneratedProtocolMessageType('BundleRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLEREQUEST,
  '__module__' : 'proto.api2msl_pb2'
  # @@protoc_insertion_point(class_scope:api2visual.BundleRequest)
  })
_sym_db.RegisterMessage(BundleRequest)

JsonReply = _reflection.GeneratedProtocolMessageType('JsonReply', (_message.Message,), {
  'DESCRIPTOR' : _JSONREPLY,
  '__module__' : 'proto.api2msl_pb2'
  # @@protoc_insertion_point(class_scope:api2visual.JsonReply)
  })
_sym_db.RegisterMessage(JsonReply)


DESCRIPTOR._options = None

_API2MSL = _descriptor.ServiceDescriptor(
  name='Api2Msl',
  full_name='api2visual.Api2Msl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=92,
  serialized_end=164,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetJson',
    full_name='api2visual.Api2Msl.GetJson',
    index=0,
    containing_service=None,
    input_type=_BUNDLEREQUEST,
    output_type=_JSONREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API2MSL)

DESCRIPTOR.services_by_name['Api2Msl'] = _API2MSL

# @@protoc_insertion_point(module_scope)
