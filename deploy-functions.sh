#!/bin/sh

aws cloudformation create-stack --stack-name call-center-functions --template-body file://call-center-functions.yml --capabilities CAPABILITY_IAM
aws cloudformation wait stack-create-complete --stack-name call-center-functions
