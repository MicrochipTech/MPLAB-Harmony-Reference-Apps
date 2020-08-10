#include "ack_user_config.h"
#ifdef ACK_RANGE_CONTROLLER

/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:24 2019. */

#include "V3AlexaRangeController.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t v3avs_capabilities_V3AlexaRangeController_fields[1] = {
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaRangeController_Directive_fields[4] = {
    PB_FIELD(  1, UENUM   , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaRangeController_Directive, directive_name, directive_name, 0),
    PB_ONEOF_FIELD(payload,   2, MESSAGE , ONEOF, STATIC  , OTHER, v3avs_capabilities_V3AlexaRangeController_Directive, set_range_value, directive_name, &v3avs_capabilities_V3AlexaRangeController_SetRangeValue_fields),
    PB_ONEOF_FIELD(payload,   3, MESSAGE , ONEOF, STATIC  , UNION, v3avs_capabilities_V3AlexaRangeController_Directive, adjust_range_value, directive_name, &v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaRangeController_SetRangeValue_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaRangeController_SetRangeValue, range_value, range_value, &v3avs_types_V3Range_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue, range_delta, range_delta, &v3avs_types_V3RangeDelta_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaRangeController_Event_fields[1] = {
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaRangeController_RangeValueProperty_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaRangeController_RangeValueProperty, range_value, range_value, &v3avs_types_V3Range_fields),
    PB_LAST_FIELD
};




/* Check that field information fits in pb_field_t */
#if !defined(PB_FIELD_32BIT)
/* If you get an error here, it means that you need to define PB_FIELD_32BIT
 * compile-time option. You can do that in pb.h or on compiler command line.
 *
 * The reason you need to do this is that some of your messages contain tag
 * numbers or field sizes that are larger than what can fit in 8 or 16 bit
 * field descriptors.
 */
PB_STATIC_ASSERT((pb_membersize(v3avs_capabilities_V3AlexaRangeController_Directive, payload.set_range_value) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_Directive, payload.adjust_range_value) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_SetRangeValue, range_value) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue, range_delta) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_RangeValueProperty, range_value) < 65536), YOU_MUST_DEFINE_PB_FIELD_32BIT_FOR_MESSAGES_v3avs_capabilities_V3AlexaRangeController_v3avs_capabilities_V3AlexaRangeController_Directive_v3avs_capabilities_V3AlexaRangeController_SetRangeValue_v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue_v3avs_capabilities_V3AlexaRangeController_Event_v3avs_capabilities_V3AlexaRangeController_RangeValueProperty)
#endif

#if !defined(PB_FIELD_16BIT) && !defined(PB_FIELD_32BIT)
/* If you get an error here, it means that you need to define PB_FIELD_16BIT
 * compile-time option. You can do that in pb.h or on compiler command line.
 *
 * The reason you need to do this is that some of your messages contain tag
 * numbers or field sizes that are larger than what can fit in the default
 * 8 bit descriptors.
 */
PB_STATIC_ASSERT((pb_membersize(v3avs_capabilities_V3AlexaRangeController_Directive, payload.set_range_value) < 256 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_Directive, payload.adjust_range_value) < 256 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_SetRangeValue, range_value) < 256 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue, range_delta) < 256 && pb_membersize(v3avs_capabilities_V3AlexaRangeController_RangeValueProperty, range_value) < 256), YOU_MUST_DEFINE_PB_FIELD_16BIT_FOR_MESSAGES_v3avs_capabilities_V3AlexaRangeController_v3avs_capabilities_V3AlexaRangeController_Directive_v3avs_capabilities_V3AlexaRangeController_SetRangeValue_v3avs_capabilities_V3AlexaRangeController_AdjustRangeValue_v3avs_capabilities_V3AlexaRangeController_Event_v3avs_capabilities_V3AlexaRangeController_RangeValueProperty)
#endif


/* @@protoc_insertion_point(eof) */

#endif
