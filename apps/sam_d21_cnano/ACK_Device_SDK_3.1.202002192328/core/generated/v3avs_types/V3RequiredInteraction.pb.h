#include "ack_user_config.h"
#if defined(ACK_COOKING)

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Tue Aug 27 15:16:23 2019. */

#ifndef PB_V3AVS_TYPES_V3REQUIREDINTERACTION_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3REQUIREDINTERACTION_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _v3avs_types_V3RequiredInteraction_Value {
    v3avs_types_V3RequiredInteraction_Value_NONE = 0,
    v3avs_types_V3RequiredInteraction_Value_BASTE = 1,
    v3avs_types_V3RequiredInteraction_Value_CHECK = 2,
    v3avs_types_V3RequiredInteraction_Value_COVER = 3,
    v3avs_types_V3RequiredInteraction_Value_PEEL_BACK_FILM = 4,
    v3avs_types_V3RequiredInteraction_Value_POKE = 5,
    v3avs_types_V3RequiredInteraction_Value_REPLACE_FILM = 6,
    v3avs_types_V3RequiredInteraction_Value_ROTATE = 7,
    v3avs_types_V3RequiredInteraction_Value_STIR = 8,
    v3avs_types_V3RequiredInteraction_Value_TOSS = 9,
    v3avs_types_V3RequiredInteraction_Value_TURN_OVER = 10,
    v3avs_types_V3RequiredInteraction_Value_UNCOVER = 11,
    v3avs_types_V3RequiredInteraction_Value_CUSTOM = 12
} v3avs_types_V3RequiredInteraction_Value;
#define _v3avs_types_V3RequiredInteraction_Value_MIN v3avs_types_V3RequiredInteraction_Value_NONE
#define _v3avs_types_V3RequiredInteraction_Value_MAX v3avs_types_V3RequiredInteraction_Value_CUSTOM
#define _v3avs_types_V3RequiredInteraction_Value_ARRAYSIZE ((v3avs_types_V3RequiredInteraction_Value)(v3avs_types_V3RequiredInteraction_Value_CUSTOM+1))

/* Struct definitions */
typedef struct _v3avs_types_V3RequiredInteraction {
    v3avs_types_V3RequiredInteraction_Value value;
/* @@protoc_insertion_point(struct:v3avs_types_V3RequiredInteraction) */
} v3avs_types_V3RequiredInteraction;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3RequiredInteraction_init_default {(v3avs_types_V3RequiredInteraction_Value)0}
#define v3avs_types_V3RequiredInteraction_init_zero {(v3avs_types_V3RequiredInteraction_Value)0}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3RequiredInteraction_value_tag 1

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3RequiredInteraction_fields[2];

/* Maximum encoded size of messages (where known) */
#define v3avs_types_V3RequiredInteraction_size   2

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3REQUIREDINTERACTION_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
