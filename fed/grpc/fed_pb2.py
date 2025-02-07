# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fed.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fed.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\200\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tfed.proto\"S\n\x0fSendDataRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x17\n\x0fupstream_seq_id\x18\x02 \x01(\t\x12\x19\n\x11\x64ownstream_seq_id\x18\x03 \x01(\t\"\"\n\x10SendDataResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2@\n\x0bGrpcService\x12\x31\n\x08SendData\x12\x10.SendDataRequest\x1a\x11.SendDataResponse\"\x00\x42\x03\x80\x01\x01\x62\x06proto3'
)




_SENDDATAREQUEST = _descriptor.Descriptor(
  name='SendDataRequest',
  full_name='SendDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='SendDataRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upstream_seq_id', full_name='SendDataRequest.upstream_seq_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downstream_seq_id', full_name='SendDataRequest.downstream_seq_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=13,
  serialized_end=96,
)


_SENDDATARESPONSE = _descriptor.Descriptor(
  name='SendDataResponse',
  full_name='SendDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SendDataResponse.result', index=0,
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
  serialized_start=98,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['SendDataRequest'] = _SENDDATAREQUEST
DESCRIPTOR.message_types_by_name['SendDataResponse'] = _SENDDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendDataRequest = _reflection.GeneratedProtocolMessageType('SendDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDDATAREQUEST,
  '__module__' : 'fed_pb2'
  # @@protoc_insertion_point(class_scope:SendDataRequest)
  })
_sym_db.RegisterMessage(SendDataRequest)

SendDataResponse = _reflection.GeneratedProtocolMessageType('SendDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDDATARESPONSE,
  '__module__' : 'fed_pb2'
  # @@protoc_insertion_point(class_scope:SendDataResponse)
  })
_sym_db.RegisterMessage(SendDataResponse)


DESCRIPTOR._options = None

_GRPCSERVICE = _descriptor.ServiceDescriptor(
  name='GrpcService',
  full_name='GrpcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=134,
  serialized_end=198,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='GrpcService.SendData',
    index=0,
    containing_service=None,
    input_type=_SENDDATAREQUEST,
    output_type=_SENDDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCSERVICE)

DESCRIPTOR.services_by_name['GrpcService'] = _GRPCSERVICE

# @@protoc_insertion_point(module_scope)
