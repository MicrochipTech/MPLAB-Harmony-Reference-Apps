# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_types/V3Connectivity.proto

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
  name='v3avs_types/V3Connectivity.proto',
  package='v3avs_types',
  syntax='proto3',
  serialized_pb=_b('\n v3avs_types/V3Connectivity.proto\x12\x0bv3avs_types\"\xdc\x01\n\x0eV3Connectivity\x12\x42\n\x05value\x18\x01 \x01(\x0b\x32\x33.v3avs_types.V3Connectivity.V3ConnectivityValueEnum\x1a\x85\x01\n\x17V3ConnectivityValueEnum\x12H\n\x05value\x18\x01 \x01(\x0e\x32\x39.v3avs_types.V3Connectivity.V3ConnectivityValueEnum.Value\" \n\x05Value\x12\x0f\n\x0bUNREACHABLE\x10\x00\x12\x06\n\x02OK\x10\x01\x42\x33\n#com.amazon.proto.avs.v3.v3avs_typesB\x0c\x43onnectivityb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='v3avs_types.V3Connectivity.V3ConnectivityValueEnum.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNREACHABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=238,
  serialized_end=270,
)
_sym_db.RegisterEnumDescriptor(_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM_VALUE)


_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM = _descriptor.Descriptor(
  name='V3ConnectivityValueEnum',
  full_name='v3avs_types.V3Connectivity.V3ConnectivityValueEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v3avs_types.V3Connectivity.V3ConnectivityValueEnum.value', index=0,
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
    _V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM_VALUE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=270,
)

_V3CONNECTIVITY = _descriptor.Descriptor(
  name='V3Connectivity',
  full_name='v3avs_types.V3Connectivity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v3avs_types.V3Connectivity.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=270,
)

_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM.fields_by_name['value'].enum_type = _V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM_VALUE
_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM.containing_type = _V3CONNECTIVITY
_V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM_VALUE.containing_type = _V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM
_V3CONNECTIVITY.fields_by_name['value'].message_type = _V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM
DESCRIPTOR.message_types_by_name['V3Connectivity'] = _V3CONNECTIVITY

V3Connectivity = _reflection.GeneratedProtocolMessageType('V3Connectivity', (_message.Message,), dict(

  V3ConnectivityValueEnum = _reflection.GeneratedProtocolMessageType('V3ConnectivityValueEnum', (_message.Message,), dict(
    DESCRIPTOR = _V3CONNECTIVITY_V3CONNECTIVITYVALUEENUM,
    __module__ = 'v3avs_types.V3Connectivity_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_types.V3Connectivity.V3ConnectivityValueEnum)
    ))
  ,
  DESCRIPTOR = _V3CONNECTIVITY,
  __module__ = 'v3avs_types.V3Connectivity_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_types.V3Connectivity)
  ))
_sym_db.RegisterMessage(V3Connectivity)
_sym_db.RegisterMessage(V3Connectivity.V3ConnectivityValueEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.amazon.proto.avs.v3.v3avs_typesB\014Connectivity'))
# @@protoc_insertion_point(module_scope)
