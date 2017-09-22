#!/bin/bash
set -ex

# source the environment file
source environment.sh

# package the lambda functions
aws cloudformation package \
  --template-file stack.yaml \
  --output-template-file stack.new.yaml \
  --s3-bucket "$S3_BUCKET" \
  --s3-prefix "$S3_PREFIX"

# deploy the stack
aws cloudformation deploy \
  --template-file stack.new.yaml \
  --stack-name AWS-Events \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    SlackURL="$SLACK_URL" \
    EmailSenderAddress="$EMAIL_SENDER" \
    SenderPhoneID="$PHONE_SENDER"