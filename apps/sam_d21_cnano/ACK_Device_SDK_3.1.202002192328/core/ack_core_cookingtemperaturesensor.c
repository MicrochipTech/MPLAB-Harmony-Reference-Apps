/*
 * Copyright 2018-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * 
 * You may not use this file except in compliance with the terms and conditions set forth in the
 * accompanying LICENSE.TXT file. THESE MATERIALS ARE PROVIDED ON AN "AS IS" BASIS. AMAZON SPECIFICALLY
 * DISCLAIMS, WITH RESPECT TO THESE MATERIALS, ALL WARRANTIES, EXPRESS, IMPLIED, OR STATUTORY, INCLUDING
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
 */

#include "ack.h"
#include "ack_core_common.h"
#include "ack_user_config.h"
#include "ack_cooking.h"
#include "v3avs_capabilities/V3AlexaCookingTemperatureSensor.pb.h"
#include "v3avs_capabilities/V3AVS.pb.h"

#ifdef ACK_COOKING_TEMPERATURE_SENSOR

ACKError_t ACK_AddCookingTemperatureProperty(
    const ACKStateCommon_t* pCommon,
    v3avs_types_V3Temperature_Scale scale,
    float temperature)
{
    v3avs_capabilities_V3AlexaCookingTemperatureSensor_CookingTemperatureProperty property;

    ACK_REENTRY_CHECK;

    property.cooking_temperature.scale = scale;
    property.cooking_temperature.value = temperature;

    return CommonEncodeContextProperty(
        V3AVS_Namespace_V3_ALEXA_COOKING_TEMPERATURE_SENSOR,
        v3avs_capabilities_V3AlexaCookingTemperatureSensor_PropertyName_COOKING_TEMPERATURE_PROP,
        0, // instance not used for this controller
        pCommon,
        v3avs_capabilities_V3AlexaCookingTemperatureSensor_CookingTemperatureProperty_fields,
        &property);
}

#endif // def ACK_COOKING_TEMPERATURE_SENSOR
