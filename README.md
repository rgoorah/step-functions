# Step Functions Code Along

![diagram](state-machine.png)

## Step 0 - Prerequisites
[Create AWS account with IAM user that has administrator permissions](prerequisites.md)

## Step 1 - Create Lambda functions
Run the following command:

```
aws cloudformation create-stack --stack-name functions --template-body file://functions.yml --capabilities CAPABILITY_IAM
```

Verify it by running this command: `aws lambda list-functions` and also look at the AWS Web Console under 'Lambda'.

## Step 2 - Create the state machine
1. Update the state machine file with your AWS Account ID by running this script: `./replace-account-id.sh`
1. Run the following command:

```
aws cloudformation create-stack --stack-name call-center --template-body file://call-center.yml --capabilities CAPABILITY_IAM
```

Verify it by running this command: `aws stepfunctions list-state-machines` and also look at the AWS Web Console under Step Functions.

## Step 3 - Execute the state machine
* Search for Step Functions at the AWS Web Console
* Click on MyStateMachine
* Click 'Start execution'

Type this in the input box:

    {
      "inputCaseID": "001"
    }

* Click 'Start execution'

## Step 4 - Oberve the input and output of the steps
Click on any step to see the inputs and outputs

![diagram](state-machine2.png)

![diagram](state-machine3.png)
