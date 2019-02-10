aws cloudformation create-stack --stack-name call-center --template-body file://call-center.yml --capabilities CAPABILITY_IAM
aws cloudformation wait stack-create-complete --stack-name call-center
