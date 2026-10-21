"""Google Gen AI SDK — generateContent.

    pip install google-genai
    python 04_google_genai.py

The SDK appends `/v1beta/models/<model>:generateContent` itself, so pass the gateway
root. The access key travels in the `x-goog-api-key` header, which the SDK sets from
`api_key`.
"""

from google import genai
from google.genai import types

from common import GOOGLE_BASE_URL, MODEL, require_key

client = genai.Client(
    api_key=require_key(),
    http_options=types.HttpOptions(base_url=GOOGLE_BASE_URL),
)

response = client.models.generate_content(
    model=MODEL,
    contents="In one sentence, what is protocol interop?",
)

print(response.text)
