#include "ack_user_config.h"
#ifdef ACK_DASH_REPLENISHMENT

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:30 2019. */

#ifndef PB_V3AVS_TYPES_V3LEVEL_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3LEVEL_PB_H_INCLUDED
#include <pb.h>

#include "v3avs_types/V3InventoryCount.pb.h"

#include "v3avs_types/V3Weight.pb.h"

#include "v3avs_types/V3Volume.pb.h"

#include "v3avs_types/V3Percentage.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _v3avs_types_V3Level {
    pb_size_t which_payload;
    union {
        v3avs_types_V3InventoryCount count;
        v3avs_types_V3Weight weight;
        v3avs_types_V3Volume volume;
        v3avs_types_V3Percentage percentage;
    } payload;
/* @@protoc_insertion_point(struct:v3avs_types_V3Level) */
} v3avs_types_V3Level;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3Level_init_default         {0, {v3avs_types_V3InventoryCount_init_default}}
#define v3avs_types_V3Level_init_zero            {0, {v3avs_types_V3InventoryCount_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3Level_count_tag            1
#define v3avs_types_V3Level_weight_tag           2
#define v3avs_types_V3Level_volume_tag           3
#define v3avs_types_V3Level_percentage_tag       4

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3Level_fields[5];

/* Maximum encoded size of messages (where known) */
#define v3avs_types_V3Level_size                 9

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3LEVEL_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif