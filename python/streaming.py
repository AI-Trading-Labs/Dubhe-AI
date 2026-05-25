"""Streaming chat completion example."""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

stream = client.chat.completions.create(
    model="dubhe-fast",
    messages=[{"role": "user", "content": "Write a short poem about AI."}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
