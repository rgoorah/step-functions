#!/bin/sh

# replacing AWS_ACCOUNT_ID with your real id

aws_id=$(aws sts get-caller-identity --output text --query 'Account')
perl -i -pe"s/AWS_ACCOUNT_ID/$aws_id/g" call-center.yml

# This does not work on OS X ):
#sed -i -e "s/AWS_ACCOUNT_ID/$aws_id/g" call-center.yml
