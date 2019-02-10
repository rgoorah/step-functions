#!/bin/sh

aws cloudformation delete-stack --stack-name call-center
aws cloudformation delete-stack --stack-name call-center-functions
aws cloudformation wait stack-delete-complete --stack-name call-center
aws cloudformation wait stack-delete-complete --stack-name call-center-functions
