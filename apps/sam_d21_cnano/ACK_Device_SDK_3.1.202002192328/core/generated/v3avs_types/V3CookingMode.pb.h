#include "ack_user_config.h"
#if defined(ACK_COOKING) || defined(ACK_COOKING_TIME_CONTROLLER) || defined(ACK_COOKING_PRESET_CONTROLLER) || defined(ACK_COOKING_FOOD_TEMPERATURE_CONTROLLER) || defined(ACK_COOKING_TEMPERATURE_CONTROLLER)

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Tue Aug 27 15:16:15 2019. */

#ifndef PB_V3AVS_TYPES_V3COOKINGMODE_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3COOKINGMODE_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _v3avs_types_V3CookingMode_Value {
    v3avs_types_V3CookingMode_Value_TIMECOOK = 0,
    v3avs_types_V3CookingMode_Value_PRESET = 1,
    v3avs_types_V3CookingMode_Value_DEFROST = 2,
    v3avs_types_V3CookingMode_Value_REHEAT = 3,
    v3avs_types_V3CookingMode_Value_BAKE = 4,
    v3avs_types_V3CookingMode_Value_BROIL = 5,
    v3avs_types_V3CookingMode_Value_ROAST = 6,
    v3avs_types_V3CookingMode_Value_TOAST = 7,
    v3avs_types_V3CookingMode_Value_STEAM = 8,
    v3avs_types_V3CookingMode_Value_SLOWCOOK = 9,
    v3avs_types_V3CookingMode_Value_SOUS_VIDE = 10,
    v3avs_types_V3CookingMode_Value_PRESSURE = 11,
    v3avs_types_V3CookingMode_Value_SAUTE = 12,
    v3avs_types_V3CookingMode_Value_SEAR = 13,
    v3avs_types_V3CookingMode_Value_BREW = 14,
    v3avs_types_V3CookingMode_Value_SMOKE = 15,
    v3avs_types_V3CookingMode_Value_WARM = 16,
    v3avs_types_V3CookingMode_Value_CUSTOM = 17,
    v3avs_types_V3CookingMode_Value_OFF = 18,
    v3avs_types_V3CookingMode_Value_AIR_FRY = 19,
    v3avs_types_V3CookingMode_Value_BOIL = 20,
    v3avs_types_V3CookingMode_Value_BLANCH = 21,
    v3avs_types_V3CookingMode_Value_BROWN = 22,
    v3avs_types_V3CookingMode_Value_CAN = 23,
    v3avs_types_V3CookingMode_Value_CONVECTION_BAKE = 24,
    v3avs_types_V3CookingMode_Value_CONVECTION_BROIL = 25,
    v3avs_types_V3CookingMode_Value_CONVECTION_ROAST = 26,
    v3avs_types_V3CookingMode_Value_CONVECTION_STEAM = 27,
    v3avs_types_V3CookingMode_Value_CURE = 28,
    v3avs_types_V3CookingMode_Value_DEHYDRATE = 29,
    v3avs_types_V3CookingMode_Value_FERMENT = 30,
    v3avs_types_V3CookingMode_Value_FRY = 31,
    v3avs_types_V3CookingMode_Value_GRILL = 32,
    v3avs_types_V3CookingMode_Value_INCUBATE = 33,
    v3avs_types_V3CookingMode_Value_MELT = 34,
    v3avs_types_V3CookingMode_Value_PROOF = 35,
    v3avs_types_V3CookingMode_Value_SIMMER = 36,
    v3avs_types_V3CookingMode_Value_SOFTEN = 37,
    v3avs_types_V3CookingMode_Value_STERILIZE = 38,
    v3avs_types_V3CookingMode_Value_STEW = 39,
    v3avs_types_V3CookingMode_Value_STIR_FRY = 40
} v3avs_types_V3CookingMode_Value;
#define _v3avs_types_V3CookingMode_Value_MIN v3avs_types_V3CookingMode_Value_TIMECOOK
#define _v3avs_types_V3CookingMode_Value_MAX v3avs_types_V3CookingMode_Value_STIR_FRY
#define _v3avs_types_V3CookingMode_Value_ARRAYSIZE ((v3avs_types_V3CookingMode_Value)(v3avs_types_V3CookingMode_Value_STIR_FRY+1))

/* Struct definitions */
typedef struct _v3avs_types_V3CookingMode {
    v3avs_types_V3CookingMode_Value value;
    pb_callback_t custom_name;
/* @@protoc_insertion_point(struct:v3avs_types_V3CookingMode) */
} v3avs_types_V3CookingMode;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3CookingMode_init_default   {(v3avs_types_V3CookingMode_Value)0, {{NULL}, NULL}}
#define v3avs_types_V3CookingMode_init_zero      {(v3avs_types_V3CookingMode_Value)0, {{NULL}, NULL}}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3CookingMode_value_tag      1
#define v3avs_types_V3CookingMode_custom_name_tag 2

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3CookingMode_fields[3];

/* Maximum encoded size of messages (where known) */
/* v3avs_types_V3CookingMode_size depends on runtime parameters */

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3COOKINGMODE_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
