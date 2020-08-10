#include "ack_user_config.h"
#ifdef ACK_BRIGHTNESS_CONTROLLER

/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:19 2019. */

#include "V3AlexaBrightnessController.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_fields[1] = {
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_Directive_fields[4] = {
    PB_FIELD(  1, UENUM   , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaBrightnessController_Directive, directive_name, directive_name, 0),
    PB_ONEOF_FIELD(payload,   2, MESSAGE , ONEOF, STATIC  , OTHER, v3avs_capabilities_V3AlexaBrightnessController_Directive, adjust_brightness, directive_name, &v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness_fields),
    PB_ONEOF_FIELD(payload,   3, MESSAGE , ONEOF, STATIC  , UNION, v3avs_capabilities_V3AlexaBrightnessController_Directive, set_brightness, directive_name, &v3avs_capabilities_V3AlexaBrightnessController_SetBrightness_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness, brightness_delta, brightness_delta, &v3avs_types_V3BrightnessDelta_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_SetBrightness_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaBrightnessController_SetBrightness, brightness, brightness, &v3avs_types_V3Brightness_fields),
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_Event_fields[1] = {
    PB_LAST_FIELD
};

const pb_field_t v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty_fields[2] = {
    PB_FIELD(  1, MESSAGE , SINGULAR, STATIC  , FIRST, v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty, brightness, brightness, &v3avs_types_V3Brightness_fields),
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
PB_STATIC_ASSERT((pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_Directive, payload.adjust_brightness) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_Directive, payload.set_brightness) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness, brightness_delta) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_SetBrightness, brightness) < 65536 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty, brightness) < 65536), YOU_MUST_DEFINE_PB_FIELD_32BIT_FOR_MESSAGES_v3avs_capabilities_V3AlexaBrightnessController_v3avs_capabilities_V3AlexaBrightnessController_Directive_v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness_v3avs_capabilities_V3AlexaBrightnessController_SetBrightness_v3avs_capabilities_V3AlexaBrightnessController_Event_v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty)
#endif

#if !defined(PB_FIELD_16BIT) && !defined(PB_FIELD_32BIT)
/* If you get an error here, it means that you need to define PB_FIELD_16BIT
 * compile-time option. You can do that in pb.h or on compiler command line.
 *
 * The reason you need to do this is that some of your messages contain tag
 * numbers or field sizes that are larger than what can fit in the default
 * 8 bit descriptors.
 */
PB_STATIC_ASSERT((pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_Directive, payload.adjust_brightness) < 256 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_Directive, payload.set_brightness) < 256 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness, brightness_delta) < 256 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_SetBrightness, brightness) < 256 && pb_membersize(v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty, brightness) < 256), YOU_MUST_DEFINE_PB_FIELD_16BIT_FOR_MESSAGES_v3avs_capabilities_V3AlexaBrightnessController_v3avs_capabilities_V3AlexaBrightnessController_Directive_v3avs_capabilities_V3AlexaBrightnessController_AdjustBrightness_v3avs_capabilities_V3AlexaBrightnessController_SetBrightness_v3avs_capabilities_V3AlexaBrightnessController_Event_v3avs_capabilities_V3AlexaBrightnessController_BrightnessProperty)
#endif


/* @@protoc_insertion_point(eof) */

#endif
