#include "ack_user_config.h"
#ifdef ACK_DASH_REPLENISHMENT

/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:30 2019. */

#include "V3Level.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t v3avs_types_V3Level_fields[5] = {
    PB_ONEOF_FIELD(payload,   1, MESSAGE , ONEOF, STATIC  , FIRST, v3avs_types_V3Level, count, count, &v3avs_types_V3InventoryCount_fields),
    PB_ONEOF_FIELD(payload,   2, MESSAGE , ONEOF, STATIC  , UNION, v3avs_types_V3Level, weight, weight, &v3avs_types_V3Weight_fields),
    PB_ONEOF_FIELD(payload,   3, MESSAGE , ONEOF, STATIC  , UNION, v3avs_types_V3Level, volume, volume, &v3avs_types_V3Volume_fields),
    PB_ONEOF_FIELD(payload,   4, MESSAGE , ONEOF, STATIC  , UNION, v3avs_types_V3Level, percentage, percentage, &v3avs_types_V3Percentage_fields),
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
PB_STATIC_ASSERT((pb_membersize(v3avs_types_V3Level, payload.count) < 65536 && pb_membersize(v3avs_types_V3Level, payload.weight) < 65536 && pb_membersize(v3avs_types_V3Level, payload.volume) < 65536 && pb_membersize(v3avs_types_V3Level, payload.percentage) < 65536), YOU_MUST_DEFINE_PB_FIELD_32BIT_FOR_MESSAGES_v3avs_types_V3Level)
#endif

#if !defined(PB_FIELD_16BIT) && !defined(PB_FIELD_32BIT)
/* If you get an error here, it means that you need to define PB_FIELD_16BIT
 * compile-time option. You can do that in pb.h or on compiler command line.
 *
 * The reason you need to do this is that some of your messages contain tag
 * numbers or field sizes that are larger than what can fit in the default
 * 8 bit descriptors.
 */
PB_STATIC_ASSERT((pb_membersize(v3avs_types_V3Level, payload.count) < 256 && pb_membersize(v3avs_types_V3Level, payload.weight) < 256 && pb_membersize(v3avs_types_V3Level, payload.volume) < 256 && pb_membersize(v3avs_types_V3Level, payload.percentage) < 256), YOU_MUST_DEFINE_PB_FIELD_16BIT_FOR_MESSAGES_v3avs_types_V3Level)
#endif


/* @@protoc_insertion_point(eof) */

#endif