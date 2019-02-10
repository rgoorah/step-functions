# Step Functions Code Along

![diagram](state-machine.png)
* Create CloudFormation stack - ./deploy
* Clean resources - ./cleanup

## Before you begin
1) Create AWS account with IAM user that has administrator permissions:
* Search for IAM
* Click Users
* Click Add user
* User name: admin
* AWS access type: check both Programmatic access and AWS Management Console access
* Click Next:Permissions
* Click Create group
* Group name: admins, check AdministratorAccess
* Click Create group
* Click Next:Tags
* Click Next:Review
* Click Create user 
* Download .csv with credentials


2) Setup AWS CLI
Open the terminal of your laptop:
```
sudo apt install python-pip
pip install awscli --upgrade --user
aws configure
AWS Access Key ID: copy paste from the csv file
AWS Secret Access Key: copy paste from the csv file
Defualt region name: us-east-2
Default output format: hit enter
```

3) Verify that AWS CLI is working
```
aws s3 ls
```
This should display your S3 buckets. If this is a new accound you will see nothing.

## Create 5 Functions using Cloud Formation
aws cloudformation create-stack --stack-name functions --template-body file://functions.yml --capabilities CAPABILITY_IAM

Verify: `aws lambda list-functions`

## Create the call center state machine using Cloud Formation
aws cloudformation create-stack --stack-name call-center --template-body file://call-center.yml --capabilities CAPABILITY_IAM

Verify: `aws cloudformation list-stacks`

## Execute the call center state machine
* Search for Step Functions
* Click on MyStateMachine
* Click 'Start execution'

Type this in the input box
```
{
"inputCaseID": "001"
}
```
* Click 'Start execution'
