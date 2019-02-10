#!/bin/sh

aws cloudformation create-stack --stack-name functions --template-body file://functions.yml --capabilities CAPABILITY_IAM
aws cloudformation wait stack-create-complete --stack-name functions
