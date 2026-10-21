"""LlamaIndex — OpenAILike against the gateway.

    pip install llama-index-core llama-index-llms-openai-like
    python 06_llamaindex.py

Use `OpenAILike`, not `OpenAI`: the latter validates model names against a built-in
list, and a gateway model name is not on it.
"""

from llama_index.llms.openai_like import OpenAILike

from common import API_KEY, MODEL, OPENAI_BASE_URL

llm = OpenAILike(
    model=MODEL,
    api_base=OPENAI_BASE_URL,
    api_key=API_KEY,
    is_chat_model=True,
)

print(llm.complete("In one sentence, what does an LLM gateway meter?"))
