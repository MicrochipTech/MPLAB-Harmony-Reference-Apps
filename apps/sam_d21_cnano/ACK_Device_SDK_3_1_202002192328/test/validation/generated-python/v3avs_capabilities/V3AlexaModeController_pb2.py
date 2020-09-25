# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_capabilities/V3AlexaModeController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v3avs_types import V3Mode_pb2 as v3avs__types_dot_V3Mode__pb2
from v3avs_types import V3ModeDelta_pb2 as v3avs__types_dot_V3ModeDelta__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_capabilities/V3AlexaModeController.proto',
  package='v3avs_capabilities',
  syntax='proto3',
  serialized_pb=_b('\n.v3avs_capabilities/V3AlexaModeController.proto\x12\x12v3avs_capabilities\x1a\x18v3avs_types/V3Mode.proto\x1a\x1dv3avs_types/V3ModeDelta.proto\"\x8a\x04\n\x15V3AlexaModeController\x1a\xfb\x01\n\tDirective\x12O\n\x0e\x64irective_name\x18\x01 \x01(\x0e\x32\x37.v3avs_capabilities.V3AlexaModeController.DirectiveName\x12\x45\n\x08set_mode\x18\x02 \x01(\x0b\x32\x31.v3avs_capabilities.V3AlexaModeController.SetModeH\x00\x12K\n\x0b\x61\x64just_mode\x18\x03 \x01(\x0b\x32\x34.v3avs_capabilities.V3AlexaModeController.AdjustModeH\x00\x42\t\n\x07payload\x1a\x07\n\x05\x45vent\x1a,\n\x07SetMode\x12!\n\x04mode\x18\x01 \x01(\x0b\x32\x13.v3avs_types.V3Mode\x1a:\n\nAdjustMode\x12,\n\nmode_delta\x18\x01 \x01(\x0b\x32\x18.v3avs_types.V3ModeDelta\x1a\x31\n\x0cModeProperty\x12!\n\x04mode\x18\x01 \x01(\x0b\x32\x13.v3avs_types.V3Mode\".\n\rDirectiveName\x12\x0c\n\x08SET_MODE\x10\x00\x12\x0f\n\x0b\x41\x44JUST_MODE\x10\x01\"\x1d\n\x0cPropertyName\x12\r\n\tMODE_PROP\x10\x00\x42\x41\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\x13\x41lexaModeControllerb\x06proto3')
  ,
  dependencies=[v3avs__types_dot_V3Mode__pb2.DESCRIPTOR,v3avs__types_dot_V3ModeDelta__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3ALEXAMODECONTROLLER_DIRECTIVENAME = _descriptor.EnumDescriptor(
  name='DirectiveName',
  full_name='v3avs_capabilities.V3AlexaModeController.DirectiveName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SET_MODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADJUST_MODE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=573,
  serialized_end=619,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXAMODECONTROLLER_DIRECTIVENAME)

_V3ALEXAMODECONTROLLER_PROPERTYNAME = _descriptor.EnumDescriptor(
  name='PropertyName',
  full_name='v3avs_capabilities.V3AlexaModeController.PropertyName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_PROP', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=621,
  serialized_end=650,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXAMODECONTROLLER_PROPERTYNAME)


_V3ALEXAMODECONTROLLER_DIRECTIVE = _descriptor.Descriptor(
  name='Directive',
  full_name='v3avs_capabilities.V3AlexaModeController.Directive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive_name', full_name='v3avs_capabilities.V3AlexaModeController.Directive.directive_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_mode', full_name='v3avs_capabilities.V3AlexaModeController.Directive.set_mode', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjust_mode', full_name='v3avs_capabilities.V3AlexaModeController.Directive.adjust_mode', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='v3avs_capabilities.V3AlexaModeController.Directive.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=154,
  serialized_end=405,
)

_V3ALEXAMODECONTROLLER_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='v3avs_capabilities.V3AlexaModeController.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=407,
  serialized_end=414,
)

_V3ALEXAMODECONTROLLER_SETMODE = _descriptor.Descriptor(
  name='SetMode',
  full_name='v3avs_capabilities.V3AlexaModeController.SetMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='v3avs_capabilities.V3AlexaModeController.SetMode.mode', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=416,
  serialized_end=460,
)

_V3ALEXAMODECONTROLLER_ADJUSTMODE = _descriptor.Descriptor(
  name='AdjustMode',
  full_name='v3avs_capabilities.V3AlexaModeController.AdjustMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode_delta', full_name='v3avs_capabilities.V3AlexaModeController.AdjustMode.mode_delta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=462,
  serialized_end=520,
)

_V3ALEXAMODECONTROLLER_MODEPROPERTY = _descriptor.Descriptor(
  name='ModeProperty',
  full_name='v3avs_capabilities.V3AlexaModeController.ModeProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='v3avs_capabilities.V3AlexaModeController.ModeProperty.mode', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=522,
  serialized_end=571,
)

_V3ALEXAMODECONTROLLER = _descriptor.Descriptor(
  name='V3AlexaModeController',
  full_name='v3avs_capabilities.V3AlexaModeController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_V3ALEXAMODECONTROLLER_DIRECTIVE, _V3ALEXAMODECONTROLLER_EVENT, _V3ALEXAMODECONTROLLER_SETMODE, _V3ALEXAMODECONTROLLER_ADJUSTMODE, _V3ALEXAMODECONTROLLER_MODEPROPERTY, ],
  enum_types=[
    _V3ALEXAMODECONTROLLER_DIRECTIVENAME,
    _V3ALEXAMODECONTROLLER_PROPERTYNAME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=650,
)

_V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['directive_name'].enum_type = _V3ALEXAMODECONTROLLER_DIRECTIVENAME
_V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['set_mode'].message_type = _V3ALEXAMODECONTROLLER_SETMODE
_V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['adjust_mode'].message_type = _V3ALEXAMODECONTROLLER_ADJUSTMODE
_V3ALEXAMODECONTROLLER_DIRECTIVE.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['set_mode'])
_V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['set_mode'].containing_oneof = _V3ALEXAMODECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXAMODECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['adjust_mode'])
_V3ALEXAMODECONTROLLER_DIRECTIVE.fields_by_name['adjust_mode'].containing_oneof = _V3ALEXAMODECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXAMODECONTROLLER_EVENT.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_SETMODE.fields_by_name['mode'].message_type = v3avs__types_dot_V3Mode__pb2._V3MODE
_V3ALEXAMODECONTROLLER_SETMODE.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_ADJUSTMODE.fields_by_name['mode_delta'].message_type = v3avs__types_dot_V3ModeDelta__pb2._V3MODEDELTA
_V3ALEXAMODECONTROLLER_ADJUSTMODE.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_MODEPROPERTY.fields_by_name['mode'].message_type = v3avs__types_dot_V3Mode__pb2._V3MODE
_V3ALEXAMODECONTROLLER_MODEPROPERTY.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_DIRECTIVENAME.containing_type = _V3ALEXAMODECONTROLLER
_V3ALEXAMODECONTROLLER_PROPERTYNAME.containing_type = _V3ALEXAMODECONTROLLER
DESCRIPTOR.message_types_by_name['V3AlexaModeController'] = _V3ALEXAMODECONTROLLER

V3AlexaModeController = _reflection.GeneratedProtocolMessageType('V3AlexaModeController', (_message.Message,), dict(

  Directive = _reflection.GeneratedProtocolMessageType('Directive', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXAMODECONTROLLER_DIRECTIVE,
    __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController.Directive)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXAMODECONTROLLER_EVENT,
    __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController.Event)
    ))
  ,

  SetMode = _reflection.GeneratedProtocolMessageType('SetMode', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXAMODECONTROLLER_SETMODE,
    __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController.SetMode)
    ))
  ,

  AdjustMode = _reflection.GeneratedProtocolMessageType('AdjustMode', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXAMODECONTROLLER_ADJUSTMODE,
    __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController.AdjustMode)
    ))
  ,

  ModeProperty = _reflection.GeneratedProtocolMessageType('ModeProperty', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXAMODECONTROLLER_MODEPROPERTY,
    __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController.ModeProperty)
    ))
  ,
  DESCRIPTOR = _V3ALEXAMODECONTROLLER,
  __module__ = 'v3avs_capabilities.V3AlexaModeController_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaModeController)
  ))
_sym_db.RegisterMessage(V3AlexaModeController)
_sym_db.RegisterMessage(V3AlexaModeController.Directive)
_sym_db.RegisterMessage(V3AlexaModeController.Event)
_sym_db.RegisterMessage(V3AlexaModeController.SetMode)
_sym_db.RegisterMessage(V3AlexaModeController.AdjustMode)
_sym_db.RegisterMessage(V3AlexaModeController.ModeProperty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\023AlexaModeController'))
# @@protoc_insertion_point(module_scope)