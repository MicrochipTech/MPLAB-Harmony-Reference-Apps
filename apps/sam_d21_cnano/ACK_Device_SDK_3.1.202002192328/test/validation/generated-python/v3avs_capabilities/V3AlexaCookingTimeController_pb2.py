# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3avs_capabilities/V3AlexaCookingTimeController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v3avs_types import V3CookingMode_pb2 as v3avs__types_dot_V3CookingMode__pb2
from v3avs_types import V3EnumeratedPowerLevel_pb2 as v3avs__types_dot_V3EnumeratedPowerLevel__pb2
from v3avs_types import V3FoodItem_pb2 as v3avs__types_dot_V3FoodItem__pb2
from v3avs_types import V3IntegralPowerLevel_pb2 as v3avs__types_dot_V3IntegralPowerLevel__pb2
from v3avs_types import V3Duration_pb2 as v3avs__types_dot_V3Duration__pb2
from v3avs_types import V3Temperature_pb2 as v3avs__types_dot_V3Temperature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3avs_capabilities/V3AlexaCookingTimeController.proto',
  package='v3avs_capabilities',
  syntax='proto3',
  serialized_pb=_b('\n5v3avs_capabilities/V3AlexaCookingTimeController.proto\x12\x12v3avs_capabilities\x1a\x1fv3avs_types/V3CookingMode.proto\x1a(v3avs_types/V3EnumeratedPowerLevel.proto\x1a\x1cv3avs_types/V3FoodItem.proto\x1a&v3avs_types/V3IntegralPowerLevel.proto\x1a\x1cv3avs_types/V3Duration.proto\x1a\x1fv3avs_types/V3Temperature.proto\"\xfa\n\n\x1cV3AlexaCookingTimeController\x1a\xa0\x02\n\tDirective\x12V\n\x0e\x64irective_name\x18\x01 \x01(\x0e\x32>.v3avs_capabilities.V3AlexaCookingTimeController.DirectiveName\x12S\n\x0c\x63ook_by_time\x18\x02 \x01(\x0b\x32;.v3avs_capabilities.V3AlexaCookingTimeController.CookByTimeH\x00\x12[\n\x10\x61\x64just_cook_time\x18\x03 \x01(\x0b\x32?.v3avs_capabilities.V3AlexaCookingTimeController.AdjustCookTimeH\x00\x42\t\n\x07payload\x1a\x07\n\x05\x45vent\x1a\x92\x02\n\x11\x43ookingPowerLevel\x12h\n\x18\x63ooking_power_level_type\x18\x01 \x01(\x0e\x32\x46.v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevelType\x12\x45\n\x16\x65numerated_power_level\x18\x02 \x01(\x0b\x32#.v3avs_types.V3EnumeratedPowerLevelH\x00\x12\x41\n\x14integral_power_level\x18\x03 \x01(\x0b\x32!.v3avs_types.V3IntegralPowerLevelH\x00\x42\t\n\x07payload\x1a\xb7\x02\n\nCookByTime\x12*\n\tcook_time\x18\x01 \x01(\x0b\x32\x17.v3avs_types.V3Duration\x12\x30\n\x0c\x63ooking_mode\x18\x02 \x01(\x0b\x32\x1a.v3avs_types.V3CookingMode\x12_\n\x13\x63ooking_power_level\x18\x03 \x01(\x0b\x32\x42.v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel\x12*\n\tfood_item\x18\x04 \x01(\x0b\x32\x17.v3avs_types.V3FoodItem\x12>\n\x1atarget_cooking_temperature\x18\x05 \x01(\x0b\x32\x1a.v3avs_types.V3Temperature\x1a\x42\n\x0e\x41\x64justCookTime\x12\x30\n\x0f\x63ook_time_delta\x18\x01 \x01(\x0b\x32\x17.v3avs_types.V3Duration\x1aQ\n\x19RequestedCookTimeProperty\x12\x34\n\x13requested_cook_time\x18\x01 \x01(\x0b\x32\x17.v3avs_types.V3Duration\x1at\n\x19\x43ookingPowerLevelProperty\x12W\n\x0bpower_level\x18\x01 \x01(\x0b\x32\x42.v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel\"7\n\rDirectiveName\x12\x10\n\x0c\x43OOK_BY_TIME\x10\x00\x12\x14\n\x10\x41\x44JUST_COOK_TIME\x10\x01\"M\n\x15\x43ookingPowerLevelType\x12\x1a\n\x16\x45NUMERATED_POWER_LEVEL\x10\x00\x12\x18\n\x14INTEGRAL_POWER_LEVEL\x10\x01\"J\n\x0cPropertyName\x12\x1c\n\x18REQUESTED_COOK_TIME_PROP\x10\x00\x12\x1c\n\x18\x43OOKING_POWER_LEVEL_PROP\x10\x01\x42H\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\x1a\x41lexaCookingTimeControllerb\x06proto3')
  ,
  dependencies=[v3avs__types_dot_V3CookingMode__pb2.DESCRIPTOR,v3avs__types_dot_V3EnumeratedPowerLevel__pb2.DESCRIPTOR,v3avs__types_dot_V3FoodItem__pb2.DESCRIPTOR,v3avs__types_dot_V3IntegralPowerLevel__pb2.DESCRIPTOR,v3avs__types_dot_V3Duration__pb2.DESCRIPTOR,v3avs__types_dot_V3Temperature__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVENAME = _descriptor.EnumDescriptor(
  name='DirectiveName',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.DirectiveName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COOK_BY_TIME', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADJUST_COOK_TIME', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1478,
  serialized_end=1533,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVENAME)

_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELTYPE = _descriptor.EnumDescriptor(
  name='CookingPowerLevelType',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUMERATED_POWER_LEVEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGRAL_POWER_LEVEL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1535,
  serialized_end=1612,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELTYPE)

_V3ALEXACOOKINGTIMECONTROLLER_PROPERTYNAME = _descriptor.EnumDescriptor(
  name='PropertyName',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.PropertyName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUESTED_COOK_TIME_PROP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOKING_POWER_LEVEL_PROP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1614,
  serialized_end=1688,
)
_sym_db.RegisterEnumDescriptor(_V3ALEXACOOKINGTIMECONTROLLER_PROPERTYNAME)


_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE = _descriptor.Descriptor(
  name='Directive',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.Directive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive_name', full_name='v3avs_capabilities.V3AlexaCookingTimeController.Directive.directive_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cook_by_time', full_name='v3avs_capabilities.V3AlexaCookingTimeController.Directive.cook_by_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjust_cook_time', full_name='v3avs_capabilities.V3AlexaCookingTimeController.Directive.adjust_cook_time', index=2,
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
      name='payload', full_name='v3avs_capabilities.V3AlexaCookingTimeController.Directive.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=319,
  serialized_end=607,
)

_V3ALEXACOOKINGTIMECONTROLLER_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.Event',
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
  serialized_start=609,
  serialized_end=616,
)

_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL = _descriptor.Descriptor(
  name='CookingPowerLevel',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cooking_power_level_type', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel.cooking_power_level_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enumerated_power_level', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel.enumerated_power_level', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integral_power_level', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel.integral_power_level', index=2,
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
      name='payload', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=619,
  serialized_end=893,
)

_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME = _descriptor.Descriptor(
  name='CookByTime',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cook_time', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime.cook_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cooking_mode', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime.cooking_mode', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cooking_power_level', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime.cooking_power_level', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='food_item', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime.food_item', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_cooking_temperature', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookByTime.target_cooking_temperature', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=896,
  serialized_end=1207,
)

_V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME = _descriptor.Descriptor(
  name='AdjustCookTime',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.AdjustCookTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cook_time_delta', full_name='v3avs_capabilities.V3AlexaCookingTimeController.AdjustCookTime.cook_time_delta', index=0,
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
  serialized_start=1209,
  serialized_end=1275,
)

_V3ALEXACOOKINGTIMECONTROLLER_REQUESTEDCOOKTIMEPROPERTY = _descriptor.Descriptor(
  name='RequestedCookTimeProperty',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.RequestedCookTimeProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_cook_time', full_name='v3avs_capabilities.V3AlexaCookingTimeController.RequestedCookTimeProperty.requested_cook_time', index=0,
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
  serialized_start=1277,
  serialized_end=1358,
)

_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELPROPERTY = _descriptor.Descriptor(
  name='CookingPowerLevelProperty',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevelProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='power_level', full_name='v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevelProperty.power_level', index=0,
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
  serialized_start=1360,
  serialized_end=1476,
)

_V3ALEXACOOKINGTIMECONTROLLER = _descriptor.Descriptor(
  name='V3AlexaCookingTimeController',
  full_name='v3avs_capabilities.V3AlexaCookingTimeController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE, _V3ALEXACOOKINGTIMECONTROLLER_EVENT, _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL, _V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME, _V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME, _V3ALEXACOOKINGTIMECONTROLLER_REQUESTEDCOOKTIMEPROPERTY, _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELPROPERTY, ],
  enum_types=[
    _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVENAME,
    _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELTYPE,
    _V3ALEXACOOKINGTIMECONTROLLER_PROPERTYNAME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=1688,
)

_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['directive_name'].enum_type = _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVENAME
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['cook_by_time'].message_type = _V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['adjust_cook_time'].message_type = _V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['cook_by_time'])
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['cook_by_time'].containing_oneof = _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['adjust_cook_time'])
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.fields_by_name['adjust_cook_time'].containing_oneof = _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE.oneofs_by_name['payload']
_V3ALEXACOOKINGTIMECONTROLLER_EVENT.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['cooking_power_level_type'].enum_type = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELTYPE
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['enumerated_power_level'].message_type = v3avs__types_dot_V3EnumeratedPowerLevel__pb2._V3ENUMERATEDPOWERLEVEL
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['integral_power_level'].message_type = v3avs__types_dot_V3IntegralPowerLevel__pb2._V3INTEGRALPOWERLEVEL
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['enumerated_power_level'])
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['enumerated_power_level'].containing_oneof = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.oneofs_by_name['payload']
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.oneofs_by_name['payload'].fields.append(
  _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['integral_power_level'])
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.fields_by_name['integral_power_level'].containing_oneof = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL.oneofs_by_name['payload']
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.fields_by_name['cook_time'].message_type = v3avs__types_dot_V3Duration__pb2._V3DURATION
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.fields_by_name['cooking_mode'].message_type = v3avs__types_dot_V3CookingMode__pb2._V3COOKINGMODE
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.fields_by_name['cooking_power_level'].message_type = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.fields_by_name['food_item'].message_type = v3avs__types_dot_V3FoodItem__pb2._V3FOODITEM
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.fields_by_name['target_cooking_temperature'].message_type = v3avs__types_dot_V3Temperature__pb2._V3TEMPERATURE
_V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME.fields_by_name['cook_time_delta'].message_type = v3avs__types_dot_V3Duration__pb2._V3DURATION
_V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_REQUESTEDCOOKTIMEPROPERTY.fields_by_name['requested_cook_time'].message_type = v3avs__types_dot_V3Duration__pb2._V3DURATION
_V3ALEXACOOKINGTIMECONTROLLER_REQUESTEDCOOKTIMEPROPERTY.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELPROPERTY.fields_by_name['power_level'].message_type = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELPROPERTY.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVENAME.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELTYPE.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
_V3ALEXACOOKINGTIMECONTROLLER_PROPERTYNAME.containing_type = _V3ALEXACOOKINGTIMECONTROLLER
DESCRIPTOR.message_types_by_name['V3AlexaCookingTimeController'] = _V3ALEXACOOKINGTIMECONTROLLER

V3AlexaCookingTimeController = _reflection.GeneratedProtocolMessageType('V3AlexaCookingTimeController', (_message.Message,), dict(

  Directive = _reflection.GeneratedProtocolMessageType('Directive', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_DIRECTIVE,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.Directive)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_EVENT,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.Event)
    ))
  ,

  CookingPowerLevel = _reflection.GeneratedProtocolMessageType('CookingPowerLevel', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVEL,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevel)
    ))
  ,

  CookByTime = _reflection.GeneratedProtocolMessageType('CookByTime', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_COOKBYTIME,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.CookByTime)
    ))
  ,

  AdjustCookTime = _reflection.GeneratedProtocolMessageType('AdjustCookTime', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_ADJUSTCOOKTIME,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.AdjustCookTime)
    ))
  ,

  RequestedCookTimeProperty = _reflection.GeneratedProtocolMessageType('RequestedCookTimeProperty', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_REQUESTEDCOOKTIMEPROPERTY,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.RequestedCookTimeProperty)
    ))
  ,

  CookingPowerLevelProperty = _reflection.GeneratedProtocolMessageType('CookingPowerLevelProperty', (_message.Message,), dict(
    DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER_COOKINGPOWERLEVELPROPERTY,
    __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
    # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController.CookingPowerLevelProperty)
    ))
  ,
  DESCRIPTOR = _V3ALEXACOOKINGTIMECONTROLLER,
  __module__ = 'v3avs_capabilities.V3AlexaCookingTimeController_pb2'
  # @@protoc_insertion_point(class_scope:v3avs_capabilities.V3AlexaCookingTimeController)
  ))
_sym_db.RegisterMessage(V3AlexaCookingTimeController)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.Directive)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.Event)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.CookingPowerLevel)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.CookByTime)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.AdjustCookTime)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.RequestedCookTimeProperty)
_sym_db.RegisterMessage(V3AlexaCookingTimeController.CookingPowerLevelProperty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*com.amazon.proto.avs.v3.v3avs_capabilitiesB\032AlexaCookingTimeController'))
# @@protoc_insertion_point(module_scope)
