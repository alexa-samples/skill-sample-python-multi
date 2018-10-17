// -*- coding: utf-8 -*-

// Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

// Licensed under the Amazon Software License (the "License"). You may not use this file except in
// compliance with the License. A copy of the License is located at

//    http://aws.amazon.com/asl/

// or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific
// language governing permissions and limitations under the License.

const os = require('os');

let AWS = require('aws-sdk');
AWS.config.update({region: 'us-east-1'});
let sqs = new AWS.SQS({apiVersion: '2012-11-05'});
let sqsQueueUrl = 'https://sqs.us-east-1.amazonaws.com/XXXXXXXXXXXX/BeeperEventQueue';

const player = require('node-wav-player');
let childProcess = require('child_process');

var isBeeping = false;

// Play a beep
async function beep(wave_file) {

    player.play({
        path: wave_file,
    }).then(() => {
        if (wave_file === "404.wav")
            console.log("BOOP");
        else
            console.log("BEEP");
    }).catch((error) => {
        console.error(error);
    });

    await sleep(1000);
}

// Sleep for given milliseconds
function sleep(ms) {
    return new Promise(resolve => {
        setTimeout(resolve, ms)
    })
}

// Delete a message
function sqsDelete(receiptHandle) {

    var deleteParams = {
        QueueUrl: sqsQueueUrl,
        ReceiptHandle: receiptHandle
    };

    return sqs.deleteMessage(deleteParams, function (err, data) {
        if (err) {
            console.log("Delete Error", err);
        } else {
            console.log("Message Deleted", data);
        }
    });
}

// Read a Message
function sqsRead() {

    console.log("Listening for a new message");

    let receiveParams = {
        QueueUrl: sqsQueueUrl,
        AttributeNames: ['All'],
        MessageAttributeNames: ['All'],
        MaxNumberOfMessages: 1,
        VisibilityTimeout: 1,
        WaitTimeSeconds: 20
    };

    return sqs.receiveMessage(receiveParams, function (err, data) {
        if (err) {
            console.log("Receive Error", err);
        }
        else if (data.Messages) {

            let body = JSON.parse(data.Messages[0].Body);
            let endpoint_id = body.endpoint_id;
            let command = body.state;

            if (endpoint_id === 'computer') {

                if (command === 'BEEP')
                    console.log('Beeping!');
                beep('808.wav');

                if (command === 'BEEPER_OFF') {
                    console.log('Turning OFF Beeper');
                    stopBeeper()
                }

                if (command === 'BEEPER_ON') {
                    console.log('Turning ON Beeper');
                    startBeeper();
                }

                if (command === 'LOCK') {
                    print('Locking Computer');
                    lockComputer()
                }

                if (command === 'OPEN') {
                    print('Opening File');
                    openFile("YOUR/FILE/PATH/HERE");
                }
            }

            // Delete the message
            sqsDelete(data.Messages[0].ReceiptHandle);
        }

        // After handling the message, read another one
        sqsRead();
    });
}

async function runBeeper() {
    let waveFile = '404.wav';
    while (isBeeping) {
        await beep(waveFile);
        waveFile = (waveFile === '404.wav' ? '808.wav' : '404.wav');
    }
}

async function startBeeper() {
    isBeeping = true;
    runBeeper();
}

async function stopBeeper() {
    isBeeping = false;
}

// Lock a Windows or macOS computer
function lockComputer() {
    if (os.platform() === 'Win32')
        childProcess.exec('rundll32.exe user32.dll,LockWorkStation');
    else
        childProcess.exec('"/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession" -suspend', (error) => {
            if (error) {
                console.log('error:', error);
            }
        });

}

// Start a file using an OS platform exec
function openFile(filePath) {

    console.log(filePath);
    let command = filePath;

    if (os.platform() === 'darwin')
        command = 'open ' + filePath;

    childProcess.exec(command, (error) => {
        if (error) {
            console.log('error:', error);
        }
    });

}

function main() {
    sqsRead();
}

main();
