"""Anthropic SDK — Messages API.

    pip install anthropic
    python 03_anthropic_messages.py

Note the base URL: the Anthropic SDK appends `/v1/messages` itself, so pass the gateway
root, **not** `<root>/v1` — the opposite of the OpenAI SDK.
"""

import anthropic

from common import ANTHROPIC_BASE_URL, MODEL, require_key

client = anthropic.Anthropic(base_url=ANTHROPIC_BASE_URL, api_key=require_key())

message = client.messages.create(
    model=MODEL,
    max_tokens=512,
    messages=[{"role": "user", "content": "In one sentence, what does a gateway do?"}],
)

# Thinking blocks can come back before the text block, so take the first text block
# rather than assuming content[0] is the answer.
text = next(block.text for block in message.content if block.type == "text")
print(text)
print("model:", message.model, "| tokens:", message.usage.input_tokens + message.usage.output_tokens)
