# 10. Review the Logs

To see the results of your skill's interactions with AWS Lambda, you can review the logs.

## Review the Amazon CloudWatch logs

To see the log output of your skill handler, look to Amazon CloudWatch where the logs are collected.

1. Browse to the Lambda function page for *skill-sample-python-multi* at [https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/skill-sample-python-multi?tab=graph) (US) or [https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph](https://console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/skill-sample-python-multi?tab=graph) (EU).
2. Select the *Monitoring* tab.
3. Click the **View logs in CloudWatch** button.
4. Select the current *$LATEST* log stream.
5. Review the latest log for any errors. For any errors you find, look at the response your Lambda returned. Is the response correct?

## Test again by Sending an Utterances to Alexa
1. Navigate to the ASK developer console at [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask) and select the *Pager* skill.
2. Open the **Test** tab from the top menu.
3. Type or say the following to test the skill:
	- Custom: `ask pager to beep`
	- Custom: `ask pager to beep once`
	- Smart Home: `turn on pager`
	- Smart Home: `turn off pager`

For the custom model, if successful, Alexa should respond with "Beeping!" and a tone should play from your computer.
For the smart home model, if successful, Alexa should respond with "OK" and turn on or turn off the beeping on your computer.

## Checkpoint
You should now have a skill that beeps at you!

## Cleanup
If you want to remove the sample and cleanup the backend:
1. Close any open instance of `setup.txt`
2. Delete the working directory from your desktop
3. From the Alexa Developer Console, select and then delete the `Pager` skill.
4. In the CloudFormation console, select `skill-sample-python-multi` and then **Delete Stack** from the Actions dropdown.

## Extra Work
- Implement another intent that passes back a different command to the client via session attributes.
- Implement the [Alexa Smart Home Lock Controller interface](https://developer.amazon.com/docs/device-apis/alexa-lockcontroller.html) to utilize the `lockComputer` function in the client code.
- Use the `openFile` function in the client code using a custom model.

## Congrats, well done!!!

___
Return to the [Instructions](README.md)
