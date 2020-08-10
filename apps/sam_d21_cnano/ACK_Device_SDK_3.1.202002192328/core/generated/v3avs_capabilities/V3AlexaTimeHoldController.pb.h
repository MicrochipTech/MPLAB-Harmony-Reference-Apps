#include "ack_user_config.h"
#ifdef ACK_TIME_HOLD_CONTROLLER

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.9 at Tue Aug 27 15:16:12 2019. */

#ifndef PB_V3AVS_CAPABILITIES_V3ALEXATIMEHOLDCONTROLLER_PB_H_INCLUDED
#define PB_V3AVS_CAPABILITIES_V3ALEXATIMEHOLDCONTROLLER_PB_H_INCLUDED
#include <pb.h>

#include "v3avs_types/V3DateTime.pb.h"

#include "v3avs_types/V3Duration.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName {
    v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_HOLD = 0,
    v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_RESUME = 1
} v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName;
#define _v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_MIN v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_HOLD
#define _v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_MAX v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_RESUME
#define _v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_ARRAYSIZE ((v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName)(v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName_RESUME+1))

typedef enum _v3avs_capabilities_V3AlexaTimeHoldController_PropertyName {
    v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_HOLD_START_TIME_PROP = 0,
    v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_HOLD_END_TIME_PROP = 1
} v3avs_capabilities_V3AlexaTimeHoldController_PropertyName;
#define _v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_MIN v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_HOLD_START_TIME_PROP
#define _v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_MAX v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_HOLD_END_TIME_PROP
#define _v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_ARRAYSIZE ((v3avs_capabilities_V3AlexaTimeHoldController_PropertyName)(v3avs_capabilities_V3AlexaTimeHoldController_PropertyName_HOLD_END_TIME_PROP+1))

/* Struct definitions */
typedef struct _v3avs_capabilities_V3AlexaTimeHoldController {
    char dummy_field;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController) */
} v3avs_capabilities_V3AlexaTimeHoldController;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_Event {
    char dummy_field;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_Event) */
} v3avs_capabilities_V3AlexaTimeHoldController_Event;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_Resume {
    char dummy_field;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_Resume) */
} v3avs_capabilities_V3AlexaTimeHoldController_Resume;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_Hold {
    v3avs_types_V3DateTime hold_start_time;
    v3avs_types_V3Duration hold_duration;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_Hold) */
} v3avs_capabilities_V3AlexaTimeHoldController_Hold;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty {
    v3avs_types_V3DateTime hold_end_time;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty) */
} v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty {
    v3avs_types_V3DateTime hold_start_time;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty) */
} v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty;

typedef struct _v3avs_capabilities_V3AlexaTimeHoldController_Directive {
    v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName directive_name;
    pb_size_t which_payload;
    union {
        v3avs_capabilities_V3AlexaTimeHoldController_Hold hold;
        v3avs_capabilities_V3AlexaTimeHoldController_Resume resume;
    } payload;
/* @@protoc_insertion_point(struct:v3avs_capabilities_V3AlexaTimeHoldController_Directive) */
} v3avs_capabilities_V3AlexaTimeHoldController_Directive;

/* Default values for struct fields */

/* Initializer values for message structs */
#define v3avs_capabilities_V3AlexaTimeHoldController_init_default {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_init_default {(v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName)0, 0, {v3avs_capabilities_V3AlexaTimeHoldController_Hold_init_default}}
#define v3avs_capabilities_V3AlexaTimeHoldController_Event_init_default {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_Hold_init_default {v3avs_types_V3DateTime_init_default, v3avs_types_V3Duration_init_default}
#define v3avs_capabilities_V3AlexaTimeHoldController_Resume_init_default {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty_init_default {v3avs_types_V3DateTime_init_default}
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty_init_default {v3avs_types_V3DateTime_init_default}
#define v3avs_capabilities_V3AlexaTimeHoldController_init_zero {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_init_zero {(v3avs_capabilities_V3AlexaTimeHoldController_DirectiveName)0, 0, {v3avs_capabilities_V3AlexaTimeHoldController_Hold_init_zero}}
#define v3avs_capabilities_V3AlexaTimeHoldController_Event_init_zero {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_Hold_init_zero {v3avs_types_V3DateTime_init_zero, v3avs_types_V3Duration_init_zero}
#define v3avs_capabilities_V3AlexaTimeHoldController_Resume_init_zero {0}
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty_init_zero {v3avs_types_V3DateTime_init_zero}
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty_init_zero {v3avs_types_V3DateTime_init_zero}

/* Field tags (for use in manual encoding/decoding) */
#define v3avs_capabilities_V3AlexaTimeHoldController_Hold_hold_start_time_tag 1
#define v3avs_capabilities_V3AlexaTimeHoldController_Hold_hold_duration_tag 2
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty_hold_end_time_tag 1
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty_hold_start_time_tag 1
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_hold_tag 2
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_resume_tag 3
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_directive_name_tag 1

/* Struct field encoding specification for nanopb */
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_fields[1];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_Directive_fields[4];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_Event_fields[1];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_Hold_fields[3];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_Resume_fields[1];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty_fields[2];
extern const pb_field_t v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty_fields[2];

/* Maximum encoded size of messages (where known) */
#define v3avs_capabilities_V3AlexaTimeHoldController_size 0
#define v3avs_capabilities_V3AlexaTimeHoldController_Directive_size 30
#define v3avs_capabilities_V3AlexaTimeHoldController_Event_size 0
#define v3avs_capabilities_V3AlexaTimeHoldController_Hold_size 26
#define v3avs_capabilities_V3AlexaTimeHoldController_Resume_size 0
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldStartTimeProperty_size 13
#define v3avs_capabilities_V3AlexaTimeHoldController_HoldEndTimeProperty_size 13

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define V3ALEXATIMEHOLDCONTROLLER_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif

#endif
