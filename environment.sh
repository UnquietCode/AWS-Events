#!/bin/bash
set -ex

export AWS_DEFAULT_PROFILE=prod

export S3_BUCKET="fabric-ops"
export S3_PREFIX="aws-events"
export SLACK_URL="https://hooks.slack.com/services/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"
export EMAIL_SENDER="ops@fabricgenomics.com"