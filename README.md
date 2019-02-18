# Step Functions Code Along

## Table of Contents

* [What is this tutorial?](#what-is-this-tutorial)
* [Step 0 - Prerequisites](#step-0---prerequisites)
* [Step 1 - Create a TweetBot](#step-1---create-a-tweetbot)
* [Step 2 - Describe the state machine](#step-2---describe-the-state-machine)
* [Step 3 - Run the state machine](#step-3---run-the-state-machine)
* [Step 4 - Observe the execution through the AWS console](#step-4---observe-the-execution-through-the-aws-console)
* [Step 5 - Add storing of the tweets to DynamoDb](#step-5---add-storing-of-the-tweets-to-dynamoDb)
* [Step 6 - Parallel running states](#step-6---parallel-running-states)
* [Step 7 - Cleanup the AWS resources](#step-7---cleanup-the-aws-resources)

## What is this tutorial?

In this code along session, you will learn how to use [AWS Step Functions](https://aws.amazon.com/step-functions) to design and run a serverless workflow that coordinates multiple AWS [Lambda functions](https://aws.amazon.com/lambda).

In our example, you are a developer who has been asked to create a serverless application to notify marketing when someone mentioned the brand on twitter. While you could have one Lambda function call the other, you worry that managing all of those connections will become challenging as the application becomes more sophisticated. Plus, any change in the flow of the application will require changes in multiple places, and you could end up writing the same code over and over again.

To solve this challenge, you decide to use AWS Step Functions. Step Functions is a serverless orchestration service that lets you easily coordinate multiple Lambda functions and other AWS services into flexible workflows that are easy to debug and easy to change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you. Step Functions also has built in retries for if your Lambda function false for whatever reason you can have Step Functions retry the execution.

In the next 30 minutes, you will create a Step Functions state machine to poll Twitter for a tweet containing the text you have provided, the state machine will then use SNS to send you a text message letting you know that someone has tweeted about your product. 

You'll use AWS Step Functions, AWS Lambda, AWS SNS, and AWS CloudFormation in this tutorial. These services are within the AWS Free Tier. 

![diagram](state-machine.png)

Let’s take a look at what this state machine does.

1. First we have a lambda function “Find Tweet” to find a relevant tweet.
2. Then we use the Step Functions built in “Wait” to wait 10 seconds.
3. The “Generate Message” lambda function will take the information from the Tweet found in step 1 and use it to generate a friendly message.
4. In the “Message” state, we will use the SNS service integration to send a text message without having to write code to connect with the SNS service.
5. Finally we will end our state machine.

## Step 0 - Prerequisites
[Create AWS account with IAM user that has administrator permissions](prerequisites.md)

## Step 1 - Create a TweetBot
1. Copy the content of [this page](https://raw.githubusercontent.com/oren/step-functions/master/state-machine-tweet-bot.yml) into a file called state-machine-tweet-bot.yml

2. Create the CloudFormation stack for the Lambda functions:
```
aws cloudformation create-stack --stack-name TweetBot --template-body file://state-machine-tweet-bot.yml --capabilities CAPABILITY_IAM
```

Verify it by running this command: `aws lambda list-functions` and also look at the AWS Web Console under 'Lambda'.

## Step 2 - Describe the state machine
1. Get a list of state machines using the AWS Step Functions API:

```
aws stepfunctions list-state-machines
```

2. You should have a state machine called “TweetBot”. Find the ARN returned by the list API and use it to describe the state machine definition using the AWS Step Functions API:

```
aws stepfunctions describe-state-machine --state-machine-arn arn:aws:states:us-west-2:<YOUR_ACCOUNT_#>:stateMachine:TweetBot
```

## Step 3 - Run the state machine
1. Let’s execute the newly created state machine. We will pass it in a search text that we are looking for and a phone number we’d like to message:

```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-west-2:<YOUR_ACCOUNT_#>:stateMachine:TweetBot --input '{ "searchText": "AWS Step Functions", "phoneNumber": "<YOUR PHONE  NUMBER (ex: +1 555 444 6666)>" }'
```

## Step 4 - Observe the execution through the AWS console
1. Search for Step Functions at the AWS Web Console
2. Click on Tweetbot
3. Click 'Execution'
4. Click the first execution.

You should see something like this:

![diagram](state-machine2.png)

Green states indicate success. Red states indicate failures. The execution of each of the states can be found below in the “Execution event history”. The logs can be found in CloudWatch.

## Step 5 - Add storing of the tweets to DynamoDb

First let’s create the DynamoDb data store using CloudFormation:

1. Copy the content of [this page](https://raw.githubusercontent.com/oren/step-functions/master/tweet-datastore.yml) into a file called tweet-datastore.yml

2. Create the DynamoDB table using cloudformation:

```
aws cloudformation create-stack --stack-name TweetDataStore --template-body file://tweet-datastore.yml --capabilities CAPABILITY_IAM
```

Now we’ll update the existing state machine to store the tweets in DynamoDb using the DynamoDb service integration.

1. Copy the content of [this page](https://raw.githubusercontent.com/oren/step-functions/master/state-machine-tweet-poll-store.json) into a file called state-machine-tweet-poll-store.json

2. Update the state machine using the AWS Step Functions API:

```
aws stepfunctions update-state-machine --state-machine-arn arn:aws:states:us-west-2:<YOUR_ACCOUNT_#>:stateMachine:TweetBot --definition file://state-machine-tweet-poll-store.json
```

## Step 6 - Parallel running states

Your new state machine will look like this:

![diagram](state-machine3.png)

We have added parallel states. While the state machine is generating the SMS message to be sent, the DynamoDb service integration will also add the tweet to our newly created DynamoDb table “tweetTable”. Remember we could also add “Retry” logic to the states, in this way if we failed to write to DynamoDb or to poll a tweet, we could AWS Step Functions try again.

```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-west-2:<YOUR_ACCOUNT_#>:stateMachine:TweetBot --input '{ "searchText": "AWS Step Functions", "phoneNumber": "<YOUR PHONE  NUMBER (ex: +1 555 444 6666)>" }'
```

## Step 7 - Cleanup the AWS resources
```
aws cloudformation delete-stack --stack-name TweetBot
aws cloudformation delete-stack --stack-name TweetDataStore
```
