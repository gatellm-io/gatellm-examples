# gatellm examples

Minimal, runnable examples for a **self-hosted** [GateLLM](https://gatellm.io) gateway:
Docker / Compose deployment, the "change only `base_url`" SDK snippets, coding-agent
configuration, and transform-script templates.

Every example assumes **one** thing: you already run the gateway, and you have an access
key for it. Everything else is a single file you can copy into your own project.

- Website: <https://gatellm.io>
- Docs: <https://docs.gatellm.io/en/quickstart/docker-single-node>

## 1. Start the gateway

```bash
docker run -d \
  --name gatellm \
  -p 7890:7890 \
  -e CONSOLE_PASSWORD=change-me-on-first-login \
  -e ENCRYPTION_KEY=REPLACE_WITH_YOUR_ENCRYPTION_KEY \
  -e CONSOLE_SECRET_KEY=REPLACE_WITH_YOUR_CONSOLE_SECRET_KEY \
  -e STORAGE_MODE=sqlite \
  -v gatellm-data:/var/lib/protoflux \
  ghcr.io/gatellm-io/gatellm:latest
```

Replace the three placeholder values before running — the [install guide](https://docs.gatellm.io/en/quickstart/docker-single-node)
explains what each one is and why leaving it as-is is unsafe.

`docker/docker-compose.yml` is the same deployment with the environment in a `.env` file.

Open <http://localhost:7890>, add your upstream provider keys, then create a **gateway
access key**. The access key is what the examples read from `GATELLM_API_KEY`.

## 2. Configure

```bash
cp .env.example .env      # .env is git-ignored
export GATELLM_BASE_URL=http://localhost:7890
export GATELLM_API_KEY=sk-...
export GATELLM_MODEL=claude-opus-5    # any model name your gateway exposes
```

> Never commit a key. The examples read it from the environment only.

## 3. Base URL per protocol

The path suffix differs by SDK — each one owns its own convention:

| You use | `base_url` to configure | The SDK appends |
|---|---|---|
| OpenAI SDK / OpenAI-compatible | `${GATELLM_BASE_URL}/v1` | `/chat/completions`, `/responses`, `/embeddings`, … |
| Anthropic SDK | `${GATELLM_BASE_URL}` | `/v1/messages` |
| Google Gen AI SDK | `${GATELLM_BASE_URL}` | `/v1beta/models/…:generateContent` |
| Vercel AI SDK `createAnthropic` | `${GATELLM_BASE_URL}/v1` | `/messages` (the reverse of the Anthropic SDK) |

`python/common.py` and `typescript/src/common.ts` centralise this so no example hardcodes
it twice.

## 4. Examples

| # | Example | Python | TypeScript |
|---|---|---|---|
| 01 | OpenAI SDK — chat completion | `sdk/python/01_openai_chat.py` | `sdk/typescript/src/01-openai-chat.ts` |
| 02 | OpenAI SDK — streaming | `sdk/python/02_openai_streaming.py` | `sdk/typescript/src/02-openai-streaming.ts` |
| 03 | Anthropic SDK — messages | `sdk/python/03_anthropic_messages.py` | `sdk/typescript/src/03-anthropic-messages.ts` |
| 04 | Google Gen AI SDK — generateContent | `sdk/python/04_google_genai.py` | — |
| 05 | LangChain — `ChatOpenAI` | `sdk/python/05_langchain.py` | — |
| 06 | LlamaIndex — `OpenAILike` | `sdk/python/06_llamaindex.py` | — |
| 07 | CrewAI — `OPENAI_API_BASE` | `sdk/python/07_crewai.py` | — |
| 08 | Vercel AI SDK | — | `sdk/typescript/src/04-vercel-ai-sdk.ts` |

Run the Python ones:

```bash
cd sdk/python
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python 01_openai_chat.py
```

Run the TypeScript ones (Node 18+):

```bash
cd sdk/typescript
npm install
npm run 01
npm run typecheck
```

Each SDK has one or two traps that are not obvious from its own docs — the naming of the
model, the `/v1` suffix, which protocol an agent speaks by default. They are listed per
SDK at <https://docs.gatellm.io/en/sdk/vendor-sdks>.

## 5. Coding agents

`coding-agents/` holds the configuration for terminal agents that can point at a custom
endpoint: [Claude Code](coding-agents/claude-code/README.md),
[Codex CLI](coding-agents/codex-cli/README.md), [Gemini CLI](coding-agents/gemini-cli/README.md).
Each folder only records the config file and the variable names — the full walkthrough
lives in the docs, see <https://docs.gatellm.io/en/reference/clients-and-gateway-diffs>.

## 6. Transforms

`transforms/before-slot-transform.js` is the template for a before-slot transform script:
it runs before routing and can rewrite the request body or switch the execution model by
plan mode. Mount it on an entry model in the console.

## 7. Notes

- A model name is **whatever your gateway exposes**. The names in `.env.example` are
  placeholders from one deployment — replace them with your own, or your calls return
  `model_not_found`.
- These examples demonstrate the API surface, not billing or governance. Check the console
  for actual usage and cost.
- The gateway is self-hosted and closed-source; this repository contains examples only.

## License

MIT. See `LICENSE`.
