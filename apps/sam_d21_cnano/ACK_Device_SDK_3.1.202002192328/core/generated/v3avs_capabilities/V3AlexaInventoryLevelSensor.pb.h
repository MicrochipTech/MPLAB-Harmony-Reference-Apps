#include "ack_user_config.h"
#ifdef ACK_DASH_REPLENISHMENT

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:22 2019. */

#ifndef PB_V3AVS_CAPABILITIES_V3ALEXAINVENTORYLEVELSENSOR_PB_H_INCLUDED
#define PB_V3AVS_CAPABILITIES_V3ALEXAINVENTORYLEVELSENSOR_PB_H_INCLUDED
#include <pb.h>

#include "v3avs_types/V3Level.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName {
    v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_LEVEL_PROP = 0
} v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName;
#define _v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_MIN v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_LEVEL_PROP
#define _v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_MAX v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_LEVEL_PROP
#define _v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_ARRAYSIZE ((v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName)(v3avs_capabilities_V3AlexaInventoryLevelSensor_PropertyName_LEVEL_PROP+1))

/* Struct definitions */
typedef struct _v3avs_capabilities_V3AlexaInventoryLevelSensor {
    char dummy_field;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaInventoryLevelSensor) */
} v3avs_capabilities_V3AlexaInventoryLevelSensor;

typedef struct _v3avs_capabilities_V3AlexaInventoryLevelSensor_Event {
    char dummy_field;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaInventoryLevelSensor_Event) */
} v3avs_capabilities_V3AlexaInventoryLevelSensor_Event;

typedef struct _v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty {
    v3avs_types_V3Level level;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty) */
} v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_init_default {0}
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_Event_init_default {0}
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty_init_default {v3avs_types_V3Level_init_default}
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_init_zero {0}
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_Event_init_zero {0}
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty_init_zero {v3avs_types_V3Level_init_zero}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty_level_tag 1

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_capabilities_V3AlexaInventoryLevelSensor_fields[1];
extern const pb_field_t v3avs_capabilities_V3AlexaInventoryLevelSensor_Event_fields[1];
extern const pb_field_t v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty_fields[2];

/* Maximum encoded size of messages (where known) */
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_size 0
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_Event_size 0
#define v3avs_capabilities_V3AlexaInventoryLevelSensor_LevelProperty_size (6 + v3avs_types_V3Level_size)

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3ALEXAINVENTORYLEVELSENSOR_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
