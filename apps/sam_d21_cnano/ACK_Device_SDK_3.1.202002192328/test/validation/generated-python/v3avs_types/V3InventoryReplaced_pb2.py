# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_types/V3InventoryReplaced.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v3avs_types import V3Level_pb2 as v3avs__types_dot_V3Level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_types/V3InventoryReplaced.proto',
  package='v3avs_types',
  syntax='proto3',
  serialized_pb=_b('\n%v3avs_types/V3InventoryReplaced.proto\x12\x0bv3avs_types\x1a\x19v3avs_types/V3Level.proto\"]\n\x13V3InventoryReplaced\x12\x30\n\x12new_absolute_level\x18\x01 \x01(\x0b\x32\x14.v3avs_types.V3Level\x12\x14\n\x0creplace_date\x18\x02 \x01(\x04\x42\x38\n#com.amazon.proto.avs.v3.v3avs_typesB\x11InventoryReplacedb\x06proto3')
  ,
  dependencies=[v3avs__types_dot_V3Level__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_V3INVENTORYREPLACED = _descriptor.Descriptor(
  name='V3InventoryReplaced',
  full_name='v3avs_types.V3InventoryReplaced',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_absolute_level', full_name='v3avs_types.V3InventoryReplaced.new_absolute_level', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace_date', full_name='v3avs_types.V3InventoryReplaced.replace_date', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=174,
)

_V3INVENTORYREPLACED.fields_by_name['new_absolute_level'].message_type = v3avs__types_dot_V3Level__pb2._V3LEVEL
DESCRIPTOR.message_types_by_name['V3InventoryReplaced'] = _V3INVENTORYREPLACED

V3InventoryReplaced = _reflection.GeneratedProtocolMessageType('V3InventoryReplaced', (_message.Message,), dict(
  DESCRIPTOR = _V3INVENTORYREPLACED,
  __module__ = 'v3avs_types.V3InventoryReplaced_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_types.V3InventoryReplaced)
  ))
_sym_db.RegisterMessage(V3InventoryReplaced)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.amazon.proto.avs.v3.v3avs_typesB\021InventoryReplaced'))
# @@protoc_insertion_point(module_scope)
