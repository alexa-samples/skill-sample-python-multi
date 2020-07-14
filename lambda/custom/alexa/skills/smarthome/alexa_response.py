# -*- coding: utf-8 -*-

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/

import datetime
import math
import random
import uuid
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class AlexaResponse:
    """Helper class to generate an AlexaResponse"""

    def __init__(self, opts={}):
        
        self.context = opts.get("context", None)
        self.event = opts.get("event", None)
        
        if self.event == None:
            self.event = {
                "header": {
                    "namespace": opts.get("namespace", "Alexa"),
                    "name": opts.get("name", "Response"),
                    "messageId": opts.get("messageId", str(uuid.uuid4())),
                    "correlationToken": opts.get("correlationToken", None),
                    "payloadVersion": opts.get("payloadVersion", "3")
                },
                "endpoint": {
                    "scope": {
                        "type": "BearerToken",
                        "token": opts.get("token", "INVALID"),
                    },
                    "endpointId": opts.get("endpointId", "INVALID")
                },
                "payload": opts.get("payload", {})
            }

        # No endpoint in an AcceptGrant or Discover request
        if self.event['header']['name'] == "AcceptGrant.Response" or self.event['header']['name'] == "Discover.Response":
            del self.event['endpoint']

    def add_context_property(self, opts):
        """Add a property to the context.
        
        @param opts Contains options for the property.
        """
        if self.context is None:
            self.context = {"properties": []}

        self.context['properties'].append(self.create_context_property(opts))

    def add_payload_endpoint(self, opts):
        """Add an endpoint to the payload.
        
        @param opts Contains options for the endpoint.
        """
        if "endpoints" not in self.event['payload']:
            self.event['payload']['endpoints'] = []

        self.event['payload']['endpoints'].append(self.create_payload_endpoint(opts))

    def create_context_property(self, opts):
        """Creates a property for the context.

        @param opts Contains options for the property.
        """

        now = datetime.datetime.now()
        iso_time = now.strftime("%Y-%m-%dT%H:%M:%SZ") 

        return {
            'namespace': opts.get("namespace", "Alexa.EndpointHealth"),
            'name': opts.get("name", "connectivity"),
            'value': opts.get("value",{"value":"OK"}),
            'timeOfSample': iso_time,
            'uncertaintyInMilliseconds': opts.get("uncertaintyInMilliseconds", 0)
        }

    def create_payload_endpoint(self, opts={}):
        """Creates an endpoint for the payload.

        @param opts Contains options for the endpoint.
        """
        endpoint = {
            "capabilities": opts.get("capabilities", []),
            "description": opts.get("description", "Sample Endpoint Description"),
            "displayCategories": opts.get("displayCategories", ["OTHER"]),
            "endpointId": opts.get("endpointId", "endpoint_" + str(math.floor(random.random() * 90000 + 10000))),
            "friendlyName": opts.get("friendlyName", "Sample Endpoint"),
            "manufacturerName": opts.get("manufacturerName", "Sample Manufacturer"),
            "cookie": opts.get("cookie", {})
        }

        return endpoint

    def create_payload_endpoint_capability(self, opts={}):

        capability = {}
        capability['type'] = opts.get("type", "AlexaInterface")
        capability['interface'] = opts.get("interface", "Alexa")
        capability['version'] = opts.get("version", "3")

        supported = opts.get("supported", False)
        if supported:
            capability['properties'] = {}
            capability['properties']['supported'] = supported
            capability['properties']['proactivelyReported'] = opts.get("proactivelyReported", False)
            capability['properties']['retrievable'] = opts.get("retrievable", False)

        supportedIntents = opts.get("supportedIntents", False)
        if supportedIntents:
            capability['configuration'] = {}
            capability['configuration']['supportedIntents'] = supportedIntents
      
        return capability
