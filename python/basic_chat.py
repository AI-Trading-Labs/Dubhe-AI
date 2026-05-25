"""Basic chat completion example."""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

response = client.chat.completions.create(
    model="dubhe-fast",
    messages=[
        {"role": "user", "content": "What is the capital of Japan?"}
    ]
)
print(response.choices[0].message.content)
