#include "ack_user_config.h"
#ifdef ACK_RANGE_CONTROLLER

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:32 2019. */

#ifndef PB_V3AVS_TYPES_V3RANGE_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3RANGE_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _v3avs_types_V3Range {
    double range_value;
/* @@protoc_insertion_point(struct:v3avs_types_V3Range) */
} v3avs_types_V3Range;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3Range_init_default         {0}
#define v3avs_types_V3Range_init_zero            {0}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3Range_range_value_tag      1

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3Range_fields[2];

/* Maximum encoded size of messages (where known) */
#define v3avs_types_V3Range_size                 9

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3RANGE_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
