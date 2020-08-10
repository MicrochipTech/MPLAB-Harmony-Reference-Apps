# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_capabilities/V3AlexaColorTemperatureController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v3avs_types import V3ColorTemperatureInKelvin_pb2 as v3avs__types_dot_V3ColorTemperatureInKelvin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_capabilities/V3AlexaColorTemperatureController.proto',
  package='v3avs_capabilities',
  syntax='proto3',
  serialized_pb=_b('\n:v3avs_capabilities/V3AlexaColorTemperatureController.proto\x12\x12v3avs_capabilities\x1a,v3avs_types/V3ColorTemperatureInKelvin.proto\"\xab\x07\n!V3AlexaColorTemperatureController\x1a\xcb\x03\n\tDirective\x12[\n\x0e\x64irective_name\x18\x01 \x01(\x0e\x32\x43.v3avs_capabilities.V3AlexaColorTemperatureController.DirectiveName\x12t\n\x1a\x64\x65\x63rease_color_temperature\x18\x02 \x01(\x0b\x32N.v3avs_capabilities.V3AlexaColorTemperatureController.DecreaseColorTemperatureH\x00\x12t\n\x1aincrease_color_temperature\x18\x03 \x01(\x0b\x32N.v3avs_capabilities.V3AlexaColorTemperatureController.IncreaseColorTemperatureH\x00\x12j\n\x15set_color_temperature\x18\x04 \x01(\x0b\x32I.v3avs_capabilities.V3AlexaColorTemperatureController.SetColorTemperatureH\x00\x42\t\n\x07payload\x1a\x1a\n\x18\x44\x65\x63reaseColorTemperature\x1a\x1a\n\x18IncreaseColorTemperature\x1a\x63\n\x13SetColorTemperature\x12L\n\x1b\x63olor_temperature_in_kelvin\x18\x01 \x01(\x0b\x32\'.v3avs_types.V3ColorTemperatureInKelvin\x1a\x07\n\x05\x45vent\x1ap\n ColorTemperatureInKelvinProperty\x12L\n\x1b\x63olor_temperature_in_kelvin\x18\x01 \x01(\x0b\x32\'.v3avs_types.V3ColorTemperatureInKelvin\"j\n\rDirectiveName\x12\x1e\n\x1a\x44\x45\x43REASE_COLOR_TEMPERATURE\x10\x00\x12\x1e\n\x1aINCREASE_COLOR_TEMPERATURE\x10\x01\x12\x19\n\x15SET_COLOR_TEMPERATURE\x10\x02\"4\n\x0cPropertyName\x12$\n COLOR_TEMPERATURE_IN_KELVIN_PROP\x10\x00\x42M\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\x1f\x41lexaColorTemperatureControllerb\x06proto3')
  ,
  dependencies=[v3avs__types_dot_V3ColorTemperatureInKelvin__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVENAME = _descriptor.EnumDescriptor(
  name='DirectiveName',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.DirectiveName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DECREASE_COLOR_TEMPERATURE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCREASE_COLOR_TEMPERATURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_COLOR_TEMPERATURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=908,
  serialized_end=1014,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVENAME)

_V3ALEXACOLORTEMPERATURECONTROLLER_PROPERTYNAME = _descriptor.EnumDescriptor(
  name='PropertyName',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.PropertyName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR_TEMPERATURE_IN_KELVIN_PROP', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1016,
  serialized_end=1068,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOLORTEMPERATURECONTROLLER_PROPERTYNAME)


_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE = _descriptor.Descriptor(
  name='Directive',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive_name', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive.directive_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decrease_color_temperature', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive.decrease_color_temperature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='increase_color_temperature', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive.increase_color_temperature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_color_temperature', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive.set_color_temperature', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
      name='payload', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Directive.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=167,
  serialized_end=626,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_DECREASECOLORTEMPERATURE = _descriptor.Descriptor(
  name='DecreaseColorTemperature',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.DecreaseColorTemperature',
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
  serialized_start=628,
  serialized_end=654,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_INCREASECOLORTEMPERATURE = _descriptor.Descriptor(
  name='IncreaseColorTemperature',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.IncreaseColorTemperature',
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
  serialized_start=656,
  serialized_end=682,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE = _descriptor.Descriptor(
  name='SetColorTemperature',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.SetColorTemperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color_temperature_in_kelvin', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.SetColorTemperature.color_temperature_in_kelvin', index=0,
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
  serialized_start=684,
  serialized_end=783,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.Event',
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
  serialized_start=785,
  serialized_end=792,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_COLORTEMPERATUREINKELVINPROPERTY = _descriptor.Descriptor(
  name='ColorTemperatureInKelvinProperty',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController.ColorTemperatureInKelvinProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color_temperature_in_kelvin', full_name='v3avs_capabilities.V3AlexaColorTemperatureController.ColorTemperatureInKelvinProperty.color_temperature_in_kelvin', index=0,
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
  serialized_start=794,
  serialized_end=906,
)

_V3ALEXACOLORTEMPERATURECONTROLLER = _descriptor.Descriptor(
  name='V3AlexaColorTemperatureController',
  full_name='v3avs_capabilities.V3AlexaColorTemperatureController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE, _V3ALEXACOLORTEMPERATURECONTROLLER_DECREASECOLORTEMPERATURE, _V3ALEXACOLORTEMPERATURECONTROLLER_INCREASECOLORTEMPERATURE, _V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE, _V3ALEXACOLORTEMPERATURECONTROLLER_EVENT, _V3ALEXACOLORTEMPERATURECONTROLLER_COLORTEMPERATUREINKELVINPROPERTY, ],
  enum_types=[
    _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVENAME,
    _V3ALEXACOLORTEMPERATURECONTROLLER_PROPERTYNAME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=1068,
)

_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['directive_name'].enum_type = _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVENAME
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['decrease_color_temperature'].message_type = _V3ALEXACOLORTEMPERATURECONTROLLER_DECREASECOLORTEMPERATURE
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['increase_color_temperature'].message_type = _V3ALEXACOLORTEMPERATURECONTROLLER_INCREASECOLORTEMPERATURE
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['set_color_temperature'].message_type = _V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['decrease_color_temperature'])
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['decrease_color_temperature'].containing_oneof = _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['increase_color_temperature'])
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['increase_color_temperature'].containing_oneof = _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['set_color_temperature'])
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['set_color_temperature'].containing_oneof = _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOLORTEMPERATURECONTROLLER_DECREASECOLORTEMPERATURE.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_INCREASECOLORTEMPERATURE.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE.fields_by_name['color_temperature_in_kelvin'].message_type = v3avs__types_dot_V3ColorTemperatureInKelvin__pb2._V3COLORTEMPERATUREINKELVIN
_V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_EVENT.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_COLORTEMPERATUREINKELVINPROPERTY.fields_by_name['color_temperature_in_kelvin'].message_type = v3avs__types_dot_V3ColorTemperatureInKelvin__pb2._V3COLORTEMPERATUREINKELVIN
_V3ALEXACOLORTEMPERATURECONTROLLER_COLORTEMPERATUREINKELVINPROPERTY.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVENAME.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
_V3ALEXACOLORTEMPERATURECONTROLLER_PROPERTYNAME.containing_type = _V3ALEXACOLORTEMPERATURECONTROLLER
DESCRIPTOR.message_types_by_name['V3AlexaColorTemperatureController'] = _V3ALEXACOLORTEMPERATURECONTROLLER

V3AlexaColorTemperatureController = _reflection.GeneratedProtocolMessageType('V3AlexaColorTemperatureController', (_message.Message,), dict(

  Directive = _reflection.GeneratedProtocolMessageType('Directive', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_DIRECTIVE,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.Directive)
    ))
  ,

  DecreaseColorTemperature = _reflection.GeneratedProtocolMessageType('DecreaseColorTemperature', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_DECREASECOLORTEMPERATURE,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.DecreaseColorTemperature)
    ))
  ,

  IncreaseColorTemperature = _reflection.GeneratedProtocolMessageType('IncreaseColorTemperature', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_INCREASECOLORTEMPERATURE,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.IncreaseColorTemperature)
    ))
  ,

  SetColorTemperature = _reflection.GeneratedProtocolMessageType('SetColorTemperature', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_SETCOLORTEMPERATURE,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.SetColorTemperature)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_EVENT,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.Event)
    ))
  ,

  ColorTemperatureInKelvinProperty = _reflection.GeneratedProtocolMessageType('ColorTemperatureInKelvinProperty', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER_COLORTEMPERATUREINKELVINPROPERTY,
    __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController.ColorTemperatureInKelvinProperty)
    ))
  ,
  DESCRIPTOR = _V3ALEXACOLORTEMPERATURECONTROLLER,
  __module__ = 'v3avs_capabilities.V3AlexaColorTemperatureController_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaColorTemperatureController)
  ))
_sym_db.RegisterMessage(V3AlexaColorTemperatureController)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.Directive)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.DecreaseColorTemperature)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.IncreaseColorTemperature)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.SetColorTemperature)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.Event)
_sym_db.RegisterMessage(V3AlexaColorTemperatureController.ColorTemperatureInKelvinProperty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\037AlexaColorTemperatureController'))
# @@protoc_insertion_point(module_scope)
