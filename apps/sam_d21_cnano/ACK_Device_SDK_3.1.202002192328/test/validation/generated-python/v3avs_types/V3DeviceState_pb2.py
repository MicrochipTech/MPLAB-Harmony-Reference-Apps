# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_types/V3DeviceState.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_types/V3DeviceState.proto',
  package='v3avs_types',
  syntax='proto3',
  serialized_pb=_b('\n\x1fv3avs_types/V3DeviceState.proto\x12\x0bv3avs_types\"g\n\rV3DeviceState\x12/\n\x05value\x18\x01 \x01(\x0e\x32 .v3avs_types.V3DeviceState.Value\"%\n\x05Value\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tPREHEATED\x10\x01\x42\x32\n#com.amazon.proto.avs.v3.v3avs_typesB\x0b\x44\x65viceStateb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3DEVICESTATE_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='v3avs_types.V3DeviceState.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREHEATED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=114,
  serialized_end=151,
)
_sym_db.RegisterEnumDescriptor(_V3DEVICESTATE_VALUE)


_V3DEVICESTATE = _descriptor.Descriptor(
  name='V3DeviceState',
  full_name='v3avs_types.V3DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v3avs_types.V3DeviceState.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _V3DEVICESTATE_VALUE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=151,
)

_V3DEVICESTATE.fields_by_name['value'].enum_type = _V3DEVICESTATE_VALUE
_V3DEVICESTATE_VALUE.containing_type = _V3DEVICESTATE
DESCRIPTOR.message_types_by_name['V3DeviceState'] = _V3DEVICESTATE

V3DeviceState = _reflection.GeneratedProtocolMessageType('V3DeviceState', (_message.Message,), dict(
  DESCRIPTOR = _V3DEVICESTATE,
  __module__ = 'v3avs_types.V3DeviceState_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_types.V3DeviceState)
  ))
_sym_db.RegisterMessage(V3DeviceState)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.amazon.proto.avs.v3.v3avs_typesB\013DeviceState'))
# @@protoc_insertion_point(module_scope)