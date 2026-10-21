"""CrewAI — the gateway as an OpenAI-compatible provider.

    pip install crewai
    python 07_crewai.py

CrewAI sits on LiteLLM, so the endpoint comes from environment variables rather than a
constructor argument, and the model name carries the `openai/` prefix:

    export OPENAI_API_BASE=http://localhost:7890/v1
    export OPENAI_API_KEY=<gateway access key>
    export GATELLM_MODEL=<model your gateway exposes>
"""

import os

from crewai import Agent, Crew, Task

from common import API_KEY, MODEL, OPENAI_BASE_URL

os.environ.setdefault("OPENAI_API_BASE", OPENAI_BASE_URL)
os.environ.setdefault("OPENAI_API_KEY", API_KEY)

agent = Agent(
    role="Explainer",
    goal="Answer in one short paragraph.",
    backstory="You explain infrastructure concepts plainly.",
    llm=f"openai/{MODEL}",
)

task = Task(
    description="Explain in one paragraph what an AI gateway does for a platform team.",
    expected_output="One paragraph of plain prose.",
    agent=agent,
)

print(Crew(agents=[agent], tasks=[task]).kickoff())
