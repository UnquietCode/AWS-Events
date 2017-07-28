#!/bin/bash
set -ex

export AWS_DEFAULT_PROFILE=prod

S3_BUCKET="fabric-prod.ops"
S3_PREFIX="aws-events"
SLACK_URL="https://hooks.slack.com/services/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"

# package the lambda functions
aws cloudformation package --template-file stack.yaml --output-template-file stack.new.yaml --s3-bucket $S3_BUCKET --s3-prefix "$S3_PREFIX"

# deploy the stack
aws cloudformation deploy --template-file stack.new.yaml --stack-name AWS-Events --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides SlackURL="$SLACK_URL"