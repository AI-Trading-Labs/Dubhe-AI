"""Function calling example."""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["city"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="dubhe-fast",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools
)

msg = response.choices[0].message
if msg.tool_calls:
    for tc in msg.tool_calls:
        print(f"Call: {tc.function.name}({tc.function.arguments})")
