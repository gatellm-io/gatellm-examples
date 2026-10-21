"""OpenAI SDK — streaming.

    pip install openai
    python 02_openai_streaming.py

Streaming is passed through, so the chunks arrive as the upstream produces them.
"""

from openai import OpenAI

from common import MODEL, OPENAI_BASE_URL, require_key

client = OpenAI(base_url=OPENAI_BASE_URL, api_key=require_key())

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Count from 1 to 20, one number per line."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()
