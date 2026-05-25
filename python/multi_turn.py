"""Multi-turn conversation example."""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Dubhe AI?"},
    {"role": "assistant", "content": "Dubhe AI is an OpenAI-compatible API platform offering frontier models."},
    {"role": "user", "content": "What models do you offer?"}
]
response = client.chat.completions.create(
    model="dubhe-fast",
    messages=messages
)
print(response.choices[0].message.content)
