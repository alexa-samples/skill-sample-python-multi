# 7. Test the Code

Examine and understand the provided Lambda code.

## Examine the Code to Provide a Response to a Request

Understand how the handler properly routes and handles both a custom and smart home request by exposing custom and smart home handlers for incoming requests.

> Pressing Ctrl+/ on Windows or Cmd+/ in the inline code editor lets you comment and uncomment blocks of code.

### Import Handlers
1. Open the Lambda Console at [https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph) (US) or [https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph](https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph) (EU) and inspect the Function code section.

> If the file is not already open in the inline editor, you can open it from the file tree on the left.

This code includes the additional handlers for Session requests (Custom) and Directive requests (Smart Home).

### Handler for Smart Home Requests

The `def handler(...):` method contains an if-block, `if 'directive' in request:`, which looks for a directive, passes the request to the directive handler, and then evaluates the return response to send a message to the client.

### Handler for Custom Requests

The `def handler(...):` method also contains an, `elif 'session' in request:`, which looks for a session, passes the request to the session handler, and then evaluates the return response to send a message to the client.

## Edit the Code to Send an Event

Edit the handler code to enable sending a message to your event queue.

1. In _lambda_function.py_, confirm the `region_name` variable of `config = Config(region_name = "us-east-1")` is the same region your ran the CloudFormation script in (e.g., _us-east-1_).
2. Replace the value of the `sqs_queue_url` variable with the **[Amazon SQS Queue Url]** value from the `setup.txt` file. The value you will want to replace looks like `https://sqs.region.amazonaws.com/XXXXXXXXXXXX/PagerEventQueue`.
3. Click the **Save** button of the Lambda at the top right.

This function includes a [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) containing the [ASK SDK for Python](https://github.com/alexa/alexa-skills-kit-sdk-for-python). The code specifies your unique queue URL, and enables the SQS client to send a message to be received by your computer. 

## Test the Lambda

To test changes to the handler code, let's simulate an Alexa Request for a Smart Home message.

### Send a Smart Home Test Event

Send a simulated Alexa Smart Home Discovery request to test the Lambda.

1. Open the Lambda Console for the handler at [https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph)](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph) (US) or [https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph)](https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph) (EU).
2. Open the *Select a test event* dropdown from the top right of the menu and select **Configure test events**.
3. In the *Configure test event* dialog, create a new test event with the *Event name* of `directiveDiscovery` and paste the raw content from the file **Discovery.request.json** in the folder *instructions* ([source](https://raw.githubusercontent.com/alexa/alexa-smarthome/master/sample_messages/Discovery/Discovery.request.json)) into the text area replacing the existing placeholder content.
4. Click the **Create** button at the bottom to create the test event.
5. With the *directiveDiscovery* test selected in the dropdown, click **Test**.
6. Open the **Execution result** details to inspect the result and notice that your handler now returns a `Discover.Response` and the definition of a "Pager" device.


## Checkpoint
The skill handler code should appropriately respond to smart home messages.
 
Next to Step [8. Start the Client](start-the-client.md)

Return to the [Instructions](README.md)