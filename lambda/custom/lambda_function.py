# -*- coding: utf-8 -*-
# The skill serves as an example on how to use 
# Alexa Multi-Capability Skills (MCS) with Python

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/

import boto3
import json
import logging
import sys

from directive_handlers import *
from session_handlers import *

from ask_sdk.standard import SkillBuilder
from botocore.config import Config

sb = SkillBuilder()

config = Config(region_name = "us-east-1")

sqs_client = boto3.client("sqs", config=config)
sqs_queue_url = "https://sqs.region.amazonaws.com/XXXXXXXXXX/PagerEventQueue"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def send_message(command):
    message_body = json.dumps({"endpoint_id":"computer", "state":command})
    
    try:
        sqs_response = sqs_client.send_message(QueueUrl=sqs_queue_url, MessageBody=message_body)
    except:
        e = sys.exc_info()[0]
        logger.info("+++++ error sending message")
        logger.info(message_body)
        logger.error(e)
        return e

    logger.info("+++++ SQS Response")
    logger.info(sqs_response)

def handler(request, context): 
    logger.info("+++++ request")
    logger.info(request)
    
    if context is not None:
        logger.info("+++++ context")
        logger.info(context.__dict__)
        
    if 'directive' in request:
        logger.info("+++++ Routing Directive Handler")
        response = directive_handler(request, context)

        logger.info("+++++ response")
        logger.info(response)

        if "context" in response and "properties" in response["context"]:
            if response["context"]["properties"][0]["name"] == "powerState":
                if response["context"]["properties"][0]["value"] == "ON":
                    send_message("BEEPER_ON")
                else:
                    send_message("BEEPER_OFF")

        return response

    elif 'session' in request:
        logger.info("+++++ Routing Session Handler")
        response = session_handler(request, context)
        
        logger.info("+++++ Response")
        logger.info(response)
        
        if "command" in response["sessionAttributes"]:
            command = response["sessionAttributes"]["command"]
            logger.info(command)
            send_message(command)
    
        logger.info("+++++ response")
        return response
            
    else:
        response = None
        logger.info("+++++ Response")
        logger.info(response)
        
        return response
        