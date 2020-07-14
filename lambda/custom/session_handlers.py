# -*- coding: utf-8 -*-

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/
import logging

from ask_sdk.standard import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    speech_text = "Welcome to the Alexa Skills Kit, you can say hello!"
    
    logger.info("+++++ INSIDE LAUNCH REQUEST")

    return (
        handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .set_card(SimpleCard("Hello World", speech_text))
            .set_should_end_session(False)
            .response
    )

@sb.request_handler(can_handle_func=is_intent_name("BeepIntent"))
def beep_intent_handler(handler_input):
    """Handler for Beep Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Beeping!"

    handler_input.attributes_manager.session_attributes["command"] = "BEEP"

    return (
        handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .set_card(SimpleCard("Beeping!", speech_text))
            .set_should_end_session(False)
            .response
    )

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "You can say hello to me!"

    return (
        handler_input.response_builder
        .speak(speech_text)
        .ask(speech_text)
        .set_card(SimpleCard("Hello World", speech_text))
        .response
    )

@sb.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Goodbye!"

    return (
        handler_input.response_builder
            .speak(speech_text)
            .set_card(SimpleCard("Hello World", speech_text))
            .response
    )

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    speech_text = ("The Hello World skill can't help you with that. You can say hello!")
    reprompt = "You can say hello!"

    return (
        handler_input.response_builder
            .speak(speech_text)
            .ask(reprompt)
            .response
    )

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech_text = "Sorry, there was a problem. Please try again!"

    return (
        handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
    )

session_handler = sb.lambda_handler()
