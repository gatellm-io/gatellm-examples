"""OpenAI SDK — one chat completion, pointed at the gateway.

    pip install openai
    python 01_openai_chat.py

Only `base_url` and `api_key` change. Everything after that is ordinary OpenAI SDK code.
"""

from openai import OpenAI

from common import MODEL, OPENAI_BASE_URL, require_key

client = OpenAI(base_url=OPENAI_BASE_URL, api_key=require_key())

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "In one sentence, what is an AI gateway?"}],
)

print(response.choices[0].message.content)
print("model:", response.model, "| tokens:", response.usage.total_tokens)
