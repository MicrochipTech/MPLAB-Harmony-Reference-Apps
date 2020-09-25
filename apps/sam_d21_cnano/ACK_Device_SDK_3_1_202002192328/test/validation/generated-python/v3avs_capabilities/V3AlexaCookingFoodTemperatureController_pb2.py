# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_capabilities/V3AlexaCookingFoodTemperatureController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v3avs_types import V3Temperature_pb2 as v3avs__types_dot_V3Temperature__pb2
from v3avs_types import V3CookingMode_pb2 as v3avs__types_dot_V3CookingMode__pb2
from v3avs_types import V3FoodItem_pb2 as v3avs__types_dot_V3FoodItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_capabilities/V3AlexaCookingFoodTemperatureController.proto',
  package='v3avs_capabilities',
  syntax='proto3',
  serialized_pb=_b('\n@v3avs_capabilities/V3AlexaCookingFoodTemperatureController.proto\x12\x12v3avs_capabilities\x1a\x1fv3avs_types/V3Temperature.proto\x1a\x1fv3avs_types/V3CookingMode.proto\x1a\x1cv3avs_types/V3FoodItem.proto\"\x99\x05\n\'V3AlexaCookingFoodTemperatureController\x1a\xf0\x01\n\tDirective\x12\x61\n\x0e\x64irective_name\x18\x01 \x01(\x0e\x32I.v3avs_capabilities.V3AlexaCookingFoodTemperatureController.DirectiveName\x12u\n\x18\x63ook_by_food_temperature\x18\x02 \x01(\x0b\x32Q.v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperatureH\x00\x42\t\n\x07payload\x1a\x07\n\x05\x45vent\x1a\xb2\x01\n\x15\x43ookByFoodTemperature\x12;\n\x17target_food_temperature\x18\x01 \x01(\x0b\x32\x1a.v3avs_types.V3Temperature\x12\x30\n\x0c\x63ooking_mode\x18\x02 \x01(\x0b\x32\x1a.v3avs_types.V3CookingMode\x12*\n\tfood_item\x18\x03 \x01(\x0b\x32\x17.v3avs_types.V3FoodItem\x1a\\\n\x1dTargetFoodTemperatureProperty\x12;\n\x17target_food_temperature\x18\x01 \x01(\x0b\x32\x1a.v3avs_types.V3Temperature\"-\n\rDirectiveName\x12\x1c\n\x18\x43OOK_BY_FOOD_TEMPERATURE\x10\x00\"0\n\x0cPropertyName\x12 \n\x1cTARGET_FOOD_TEMPERATURE_PROP\x10\x00\x42S\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB%AlexaCookingFoodTemperatureControllerb\x06proto3')
  ,
  dependencies=[v3avs__types_dot_V3Temperature__pb2.DESCRIPTOR,v3avs__types_dot_V3CookingMode__pb2.DESCRIPTOR,v3avs__types_dot_V3FoodItem__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVENAME = _descriptor.EnumDescriptor(
  name='DirectiveName',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.DirectiveName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COOK_BY_FOOD_TEMPERATURE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=755,
  serialized_end=800,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVENAME)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_PROPERTYNAME = _descriptor.EnumDescriptor(
  name='PropertyName',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.PropertyName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TARGET_FOOD_TEMPERATURE_PROP', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=802,
  serialized_end=850,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_PROPERTYNAME)


_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE = _descriptor.Descriptor(
  name='Directive',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Directive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive_name', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Directive.directive_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cook_by_food_temperature', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Directive.cook_by_food_temperature', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
      name='payload', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Directive.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=229,
  serialized_end=469,
)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Event',
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
  serialized_start=471,
  serialized_end=478,
)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE = _descriptor.Descriptor(
  name='CookByFoodTemperature',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_food_temperature', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperature.target_food_temperature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cooking_mode', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperature.cooking_mode', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='food_item', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperature.food_item', index=2,
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
  ],
  serialized_start=481,
  serialized_end=659,
)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_TARGETFOODTEMPERATUREPROPERTY = _descriptor.Descriptor(
  name='TargetFoodTemperatureProperty',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.TargetFoodTemperatureProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_food_temperature', full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController.TargetFoodTemperatureProperty.target_food_temperature', index=0,
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
  serialized_start=661,
  serialized_end=753,
)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER = _descriptor.Descriptor(
  name='V3AlexaCookingFoodTemperatureController',
  full_name='v3avs_capabilities.V3AlexaCookingFoodTemperatureController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE, _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_EVENT, _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE, _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_TARGETFOODTEMPERATUREPROPERTY, ],
  enum_types=[
    _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVENAME,
    _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_PROPERTYNAME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=850,
)

_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['directive_name'].enum_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVENAME
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['cook_by_food_temperature'].message_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['cook_by_food_temperature'])
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.fields_by_name['cook_by_food_temperature'].containing_oneof = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_EVENT.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE.fields_by_name['target_food_temperature'].message_type = v3avs__types_dot_V3Temperature__pb2._V3TEMPERATURE
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE.fields_by_name['cooking_mode'].message_type = v3avs__types_dot_V3CookingMode__pb2._V3COOKINGMODE
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE.fields_by_name['food_item'].message_type = v3avs__types_dot_V3FoodItem__pb2._V3FOODITEM
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_TARGETFOODTEMPERATUREPROPERTY.fields_by_name['target_food_temperature'].message_type = v3avs__types_dot_V3Temperature__pb2._V3TEMPERATURE
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_TARGETFOODTEMPERATUREPROPERTY.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVENAME.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
_V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_PROPERTYNAME.containing_type = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER
DESCRIPTOR.message_types_by_name['V3AlexaCookingFoodTemperatureController'] = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER

V3AlexaCookingFoodTemperatureController = _reflection.GeneratedProtocolMessageType('V3AlexaCookingFoodTemperatureController', (_message.Message,), dict(

  Directive = _reflection.GeneratedProtocolMessageType('Directive', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_DIRECTIVE,
    __module__ = 'v3avs_capabilities.V3AlexaCookingFoodTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Directive)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_EVENT,
    __module__ = 'v3avs_capabilities.V3AlexaCookingFoodTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingFoodTemperatureController.Event)
    ))
  ,

  CookByFoodTemperature = _reflection.GeneratedProtocolMessageType('CookByFoodTemperature', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_COOKBYFOODTEMPERATURE,
    __module__ = 'v3avs_capabilities.V3AlexaCookingFoodTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingFoodTemperatureController.CookByFoodTemperature)
    ))
  ,

  TargetFoodTemperatureProperty = _reflection.GeneratedProtocolMessageType('TargetFoodTemperatureProperty', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER_TARGETFOODTEMPERATUREPROPERTY,
    __module__ = 'v3avs_capabilities.V3AlexaCookingFoodTemperatureController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingFoodTemperatureController.TargetFoodTemperatureProperty)
    ))
  ,
  DESCRIPTOR = _V3ALEXACOOKINGFOODTEMPERATURECONTROLLER,
  __module__ = 'v3avs_capabilities.V3AlexaCookingFoodTemperatureController_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingFoodTemperatureController)
  ))
_sym_db.RegisterMessage(V3AlexaCookingFoodTemperatureController)
_sym_db.RegisterMessage(V3AlexaCookingFoodTemperatureController.Directive)
_sym_db.RegisterMessage(V3AlexaCookingFoodTemperatureController.Event)
_sym_db.RegisterMessage(V3AlexaCookingFoodTemperatureController.CookByFoodTemperature)
_sym_db.RegisterMessage(V3AlexaCookingFoodTemperatureController.TargetFoodTemperatureProperty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB%AlexaCookingFoodTemperatureController'))
# @@protoc_insertion_point(module_scope)