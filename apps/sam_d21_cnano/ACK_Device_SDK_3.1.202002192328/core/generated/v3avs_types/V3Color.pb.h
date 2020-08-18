#include "ack_user_config.h"
#ifdef ACK_COLOR_CONTROLLER

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:25 2019. */

#ifndef PB_V3AVS_TYPES_V3COLOR_PB_H_INCLUDED
#define PB_V3AVS_TYPES_V3COLOR_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _v3avs_types_V3Color {
    double hue;
    double saturation;
    double brightness;
/* @@protoc_insertion_point(struct:v3avs_types_V3Color) */
} v3avs_types_V3Color;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_types_V3Color_init_default         {0, 0, 0}
#define v3avs_types_V3Color_init_zero            {0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_types_V3Color_hue_tag              1
#define v3avs_types_V3Color_saturation_tag       2
#define v3avs_types_V3Color_brightness_tag       3

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_types_V3Color_fields[4];

/* Maximum encoded size of messages (where known) */
#define v3avs_types_V3Color_size                 27

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3COLOR_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif