"""Error handling example."""
from openai import OpenAI, APIError, RateLimitError, APITimeoutError

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

try:
    response = client.chat.completions.create(
        model="dubhe-fast",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(response.choices[0].message.content)
except RateLimitError:
    print("Rate limited. Retrying after backoff...")
except APITimeoutError:
    print("Request timed out. Try again later.")
except APIError as e:
    print(f"API error {e.status_code}: {e.message}")
