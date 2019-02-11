# Step Functions Code Along

## Table of Contents

* [What is this tutorial?](#what-is-this-tutorial)
* [Step 0 - Prerequisites](#step-0---prerequisites)
* [Step 1 - Create Lambda functions](#step-1---create-lambda-functions)
* [Step 2 - Create the call center state machine](#step-2---create-the-call-center-state-machine)
* [Step 3 - Execute the state machine](#step-3---execute-the-state-machine)
* [Step 4 - Oberve the input and output of the states](#step-4---oberve-the-input-and-output-of-the-states)
* [Step 5 - Cleanup the AWS resources](#step-5---cleanup-the-aws-resources)

## What is this tutorial?

In this code along session, you will learn how to use [AWS Step Functions](https://aws.amazon.com/step-functions) to design and run a serverless workflow that coordinates multiple AWS [Lambda functions](https://aws.amazon.com/lambda).

In our example, you are a developer who has been asked to create a serverless application to automate handling of support tickets in a call center. While you could have one Lambda function call the other, you worry that managing all of those connections will become challenging as the call center application becomes more sophisticated. Plus, any change in the flow of the application will require changes in multiple places, and you could end up writing the same code over and over again.

To solve this challenge, you decide to use AWS Step Functions. Step Functions is a serverless orchestration service that lets you easily coordinate multiple Lambda functions into flexible workflows that are easy to debug and easy to change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you.

In the next 30 minutes, you will create a Step Functions state machine to describe the current call center process, create a few simple Lambda functions that simulate the tasks of the support team, and pass data between each Lambda function to track the progress of the support case. Then, youâ€™ll perform several tests of your workflow to observe how it responds to different inputs. Finally, youâ€™ll delete the AWS resources you used in the tutorial.

You'll use AWS Step Functions and AWS Lambda, and AWS CloudFormation in this tutorial. These services are within the AWS Free Tier.

![diagram](state-machine.png)


## Step 0 - Prerequisites
[Create AWS account with IAM user that has administrator permissions](prerequisites.md)

## Step 1 - Create Lambda functions
1) Copy the content of [this page](https://raw.githubusercontent.com/oren/step-functions/master/call-center-functions.yml) into a file called call-center-functions.yml

2) Create the CloudFormation stack for the Lambda functions:
```
aws cloudformation create-stack --stack-name call-center-functions --template-body file://call-center-functions.yml --capabilities CAPABILITY_IAM
```

Verify it by running this command: `aws lambda list-functions` and also look at the AWS Web Console under 'Lambda'.

## Step 2 - Create the call center state machine
1) Copy the content of [this page](https://raw.githubusercontent.com/oren/step-functions/master/call-center.yml) into a file called call-center.yml
2) Insert your AWS Account ID into call-center.yml file using this command:
```
perl -i -pe"s/AWS_ACCOUNT_ID/$(aws sts get-caller-identity --output text --query 'Account')/g" call-center.yml
```

3) Create the CloudFormation stack for the state machine:

```
aws cloudformation create-stack --stack-name call-center --template-body file://call-center.yml --capabilities CAPABILITY_IAM
```

Verify it by running this command: `aws stepfunctions list-state-machines` and also look at the AWS Web Console under 'Step Functions'.

## Step 3 - Execute the state machine
* Search for Step Functions at the AWS Web Console
* Click on CallCenter
* Click 'Start execution'

Type this in the input box:

    {
      "inputCaseID": "001"
    }

* Click 'Start execution'

## Step 4 - Oberve the input and output of the states
Click on any state to see the inputs and outputs

![diagram](state-machine2.png)

![diagram](state-machine3.png)

## Step 5 - Cleanup the AWS resources
```
aws cloudformation delete-stack --stack-name call-center
aws cloudformation delete-stack --stack-name call-center-functions
```
