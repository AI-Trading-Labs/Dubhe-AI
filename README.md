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

All models are accessed via their `dubhe-*` API name. Different models consume plan quota at different speeds — see [Pricing](https://dubhehub.com/pricing) for details.

| API Name | Best for | Context | Price (input/output per 1M tokens) |
|----------|----------|---------|-----------------------------------|
| `dubhe-fast` | Fast & economical chat | 1M | $0.30 / $0.60 |
| `dubhe-code` | Code generation | 200K | $0.80 / $3.00 |
| `dubhe-agent` | Agent & tool use | 205K | $1.00 / $4.00 |
| `dubhe-plus` | General purpose | 1M | $2.00 / $8.00 |
| `dubhe-omni` | Vision multimodal | 1M | $5.00 / $15.00 |
| `dubhe-reasoning` | Advanced reasoning | 1M | $6.00 / $18.00 |

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
