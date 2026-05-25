#!/bin/bash
# Basic chat completion via curl
curl https://dubhehub.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "dubhe-fast",
    "messages": [{"role": "user", "content": "What is the capital of Japan?"}]
  }'
