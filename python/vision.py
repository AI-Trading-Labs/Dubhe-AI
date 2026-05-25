"""Vision (image understanding) example. Requires dubhe-vision model."""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

response = client.chat.completions.create(
    model="dubhe-vision",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/photo.jpg"
                    }
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)
