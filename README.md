# Dubhe AI — Unified AI Infrastructure

**One API. Six frontier models. OpenAI-compatible. From $0.**

Dubhe AI provides unified access to frontier AI models through a single OpenAI-compatible API. Switch between models by changing one parameter — no SDK changes needed.

## Quick Start

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dubhehub.com/v1"
)

response = client.chat.completions.create(
    model="dubhe-fast",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

[Get your free API key →](https://dubhehub.com/signup)

## Models

| Model | Context | Best for | Price (input/output per 1M tokens) |
|-------|---------|----------|-----------------------------------|
| **Fast** | 1M | Chat, writing, everyday | $0.30 / $0.60 |
| **Reasoner** | 1M | Deep reasoning, analysis | $6.00 / $18.00 |
| **Vision** | 1M | Image understanding | $5.00 / $15.00 |
| **Code** | 200K | Programming | $0.80 / $3.00 |
| **Agent** | 205K | Autonomous workflows | $1.00 / $4.00 |
| **Omni** | 1M | Long-context tasks | $2.00 / $8.00 |

## Examples

| File | Description |
|------|-------------|
| `python/basic_chat.py` | Simple chat completion |
| `python/streaming.py` | Streaming response |
| `python/function_calling.py` | Tool/function calling |
| `python/vision.py` | Image understanding |
| `nodejs/basic_chat.mjs` | Simple chat completion |
| `nodejs/streaming.mjs` | Streaming response |
| `curl/basic_chat.sh` | Curl chat example |

## Pay-as-You-Go

No monthly commitments. Pay only for what you use. Plans start at $0 with 100K free tokens.

## Links

- [API Docs](https://dubhehub.com/docs)
- [Pricing](https://dubhehub.com/pricing)
- [Dashboard](https://dubhehub.com/dashboard)
- [Status](https://dubhehub.com/status)

---

*Built for global developers. Fair pricing. No lock-in.*
