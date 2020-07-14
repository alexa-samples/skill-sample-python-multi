# -*- coding: utf-8 -*-

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/

import logging

from alexa.skills.smarthome.alexa_response import AlexaResponse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def directive_handler(request, context):

    # Check the payload version
    if int(request['directive']['header']['payloadVersion']) != 3:
        response = AlexaResponse(
           {
                "name": "ErrorResponse",
                "payload": {
                    "type": "INTERNAL_ERROR",
                    "message": "This skill only supports Smart Home API version 3"
                }
            } 
        )
        
        return response.__dict__

    # Route based on our received Directive namespace
    namespace = request['directive']['header']['namespace']

    if namespace == "Alexa.Authorization":
        response = AlexaResponse({"namespace": "Alexa.Authorization", "name": "AcceptGrant.Response"})

        return response

    if namespace == "Alexa.Discovery":
        response = AlexaResponse({"namespace": "Alexa.Discovery", "name": "Discover.Response"})
        capability_alexa = response.create_payload_endpoint_capability()
        capability_alexa_customintent = response.create_payload_endpoint_capability({"interface": "Alexa.CustomIntent", "supportedIntents": [{"name": "BeepIntent"}]})
        capability_alexa_powercontroller = response.create_payload_endpoint_capability({"interface": "Alexa.PowerController", "supported": [{"name": "powerState"}]})
        capabilities = [capability_alexa, capability_alexa_customintent, capability_alexa_powercontroller]
        response.add_payload_endpoint({"endpointId": "pager", "friendlyName": "Pager", "description": "A computer pager", "capabilities": capabilities})
        
        return response.__dict__

    if namespace == "Alexa.PowerController":

        power_state_value = "OFF"

        if request['directive']['header']['name'] == "TurnOn":
            power_state_value = "ON"

        endpoint_id = request['directive']['endpoint']['endpointId']
        token = request['directive']['endpoint']['scope']['token']
        correlation_token = request['directive']['header']['correlationToken']

        response = AlexaResponse(
            {
                "correlationToken": correlation_token,
                "token": token,
                "endpointId": endpoint_id
            }
        )
        
        response.add_context_property({"namespace":"Alexa.PowerController", "name": "powerState", "value": power_state_value})
        
        return response.__dict__

    