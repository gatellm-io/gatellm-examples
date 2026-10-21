"""LangChain — ChatOpenAI against the gateway.

    pip install langchain-openai
    python 05_langchain.py

`ChatOpenAI` takes `base_url` (older releases: `openai_api_base`). The model name is the
one your gateway exposes, not the vendor's official id.
"""

from langchain_openai import ChatOpenAI

from common import API_KEY, MODEL, OPENAI_BASE_URL

llm = ChatOpenAI(
    model=MODEL,
    base_url=OPENAI_BASE_URL,
    api_key=API_KEY,
    temperature=0,
)

result = llm.invoke("In one sentence, why would a team put a gateway in front of LLM APIs?")
print(result.content)
