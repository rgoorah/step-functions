#!/bin/sh

aws_id=$(aws sts get-caller-identity --output text --query 'Account')
echo "$aws_id"
#sed -i -e 's/AWS_ACCOUNT_ID/$aws_id/g' call-center.yml
