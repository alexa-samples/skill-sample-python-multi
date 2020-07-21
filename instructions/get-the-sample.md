# 2. Get the Sample

Download the sample code or use git to clone the sample from the Alexa GitHub repository. You will then use the *skill-sample-python-multi* folder as a working directory for the sample.

## Download the Sample Code from GitHub

Download the zipped sample code.

1. Download the sample from [https://github.com/alexa-labs/skill-sample-python-multi/archive/master.zip](https://github.com/alexa-labs/skill-sample-python-multi/archive/master.zip).
2. Unzip the contents of `skill-sample-python-multi-master.zip`.

## (Or) Clone the Sample using Git

If you have git installed, you can use git to clone the sample instead of downloading and unzipping the archive.

1. Run the following command to clone the sample:
```
git clone https://github.com/alexa-labs/skill-sample-python-multi
```
or
```
git clone git@github.com:alexa-labs/skill-sample-python-multi.git
```
2. Once the clone is complete, you should have a folder named *skill-sample-python-multi* on your working directory.

> If you want to use Git, visit [https://git-scm.com/downloads](https://git-scm.com/downloads) to download and install a version for your platform.

## Checkpoint
- You should have a folder on your working directory like *skill-sample-python-multi-master* that contains the sample code with the `README.md` file at the root.

The sample code project structure looks like the following:

```
/client
	Contains the client script for interacting with the SQS Queue.
/cloudformation
	Contains the provisioning template for setting up backend resources.
/iam
	Contains the sample policy defining an Lambda execution role.
/instructions
	The instructions for implementing this sample.
/lambda
	The source code for the Lambda skill handler.
/models
	The custom interaction model in JSON.
README.md
	The readme for this sample.
skill.json
	The skill manifest.
```

Next to Step [3. Create the Skill](create-the-skill.md)

___
Return to the [Instructions](README.md)
