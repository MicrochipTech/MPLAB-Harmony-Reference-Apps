#include "ack_user_config.h"
#ifdef ACK_RANGE_CONTROLLER

/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.9 at Mon Jun 24 21:19:32 2019. */

#include "V3Range.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t v3avs_types_V3Range_fields[2] = {
    PB_FIELD(  1, DOUBLE  , SINGULAR, STATIC  , FIRST, v3avs_types_V3Range, range_value, range_value, 0),
    PB_LAST_FIELD
};


/* On some platforms (such as AVR), double is really float.
 * These are not directly supported by nanopb, but see example_avr_double.
 * To get rid of this error, remove any double fields from your .proto.
 */
PB_STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)

/* @@protoc_insertion_point(eof) */

#endif