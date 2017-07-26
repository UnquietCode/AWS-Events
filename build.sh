#!/bin/bash
set -ex

export AWS_DEFAULT_PROFILE=prod

S3_BUCKET="fabric-prod.ops"
S3_PREFIX="aws-events"

# package the lambda functions
aws cloudformation package --template-file stack.yaml --output-template-file stack.new.yaml --s3-bucket $S3_BUCKET --s3-prefix "$S3_PREFIX"

# deploy the stack
aws cloudformation deploy --template-file stack.new.yaml --stack-name AWS-Events --capabilities CAPABILITY_NAMED_IAM
