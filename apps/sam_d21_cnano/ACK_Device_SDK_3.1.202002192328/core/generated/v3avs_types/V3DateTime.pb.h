#include "ack_user_config.h"
#if defined(ACK_COOKING) || defined(ACK_COOKING_TIME_CONTROLLER) || defined(ACK_COOKING_PRESET_CONTROLLER) || defined(ACK_COOKING_FOOD_TEMPERATURE_CONTROLLER) || defined(ACK_COOKING_TEMPERATURE_CONTROLLER)

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Tue Aug 27 15:16:16 2019. */

#ifndef PB_V3AVS_TYPES_V3DATETIME_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3DATETIME_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _v3avs_types_V3DateTime {
    uint64_t value;
/* @@protoc_insertion_point(struct:v3avs_types_V3DateTime) */
} v3avs_types_V3DateTime;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3DateTime_init_default      {0}
#define v3avs_types_V3DateTime_init_zero         {0}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3DateTime_value_tag         1

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3DateTime_fields[2];

/* Maximum encoded size of messages (where known) */
#define v3avs_types_V3DateTime_size              11

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3DATETIME_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
