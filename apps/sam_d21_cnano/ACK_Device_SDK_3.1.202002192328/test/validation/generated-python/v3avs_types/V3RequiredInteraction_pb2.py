# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_types/V3RequiredInteraction.proto

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
  name='v3avs_types/V3RequiredInteraction.proto',
  package='v3avs_types',
  syntax='proto3',
  serialized_pb=_b('\n\'v3avs_types/V3RequiredInteraction.proto\x12\x0bv3avs_types\"\xfd\x01\n\x15V3RequiredInteraction\x12\x37\n\x05value\x18\x01 \x01(\x0e\x32(.v3avs_types.V3RequiredInteraction.Value\"\xaa\x01\n\x05Value\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x42\x41STE\x10\x01\x12\t\n\x05\x43HECK\x10\x02\x12\t\n\x05\x43OVER\x10\x03\x12\x12\n\x0ePEEL_BACK_FILM\x10\x04\x12\x08\n\x04POKE\x10\x05\x12\x10\n\x0cREPLACE_FILM\x10\x06\x12\n\n\x06ROTATE\x10\x07\x12\x08\n\x04STIR\x10\x08\x12\x08\n\x04TOSS\x10\t\x12\r\n\tTURN_OVER\x10\n\x12\x0b\n\x07UNCOVER\x10\x0b\x12\n\n\x06\x43USTOM\x10\x0c\x42:\n#com.amazon.proto.avs.v3.v3avs_typesB\x13RequiredInteractionb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3REQUIREDINTERACTION_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='v3avs_types.V3RequiredInteraction.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BASTE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COVER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEEL_BACK_FILM', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE_FILM', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STIR', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOSS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURN_OVER', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNCOVER', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_V3REQUIREDINTERACTION_VALUE)


_V3REQUIREDINTERACTION = _descriptor.Descriptor(
  name='V3RequiredInteraction',
  full_name='v3avs_types.V3RequiredInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v3avs_types.V3RequiredInteraction.value', index=0,
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
    _V3REQUIREDINTERACTION_VALUE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=310,
)

_V3REQUIREDINTERACTION.fields_by_name['value'].enum_type = _V3REQUIREDINTERACTION_VALUE
_V3REQUIREDINTERACTION_VALUE.containing_type = _V3REQUIREDINTERACTION
DESCRIPTOR.message_types_by_name['V3RequiredInteraction'] = _V3REQUIREDINTERACTION

V3RequiredInteraction = _reflection.GeneratedProtocolMessageType('V3RequiredInteraction', (_message.Message,), dict(
  DESCRIPTOR = _V3REQUIREDINTERACTION,
  __module__ = 'v3avs_types.V3RequiredInteraction_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_types.V3RequiredInteraction)
  ))
_sym_db.RegisterMessage(V3RequiredInteraction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.amazon.proto.avs.v3.v3avs_typesB\023RequiredInteraction'))
# @@protoc_insertion_point(module_scope)
