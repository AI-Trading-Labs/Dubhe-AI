#!/bin/bash
# Streaming chat completion via curl
curl -N https://dubhehub.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "dubhe-fast",
    "messages": [{"role": "user", "content": "Write a poem about AI."}],
    "stream": true
  }'
