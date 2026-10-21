# Codex CLI

Codex reads providers from `~/.codex/config.toml` and speaks the **OpenAI Responses**
protocol by default.

```toml
model = "<model your gateway exposes>"
model_provider = "gatellm"

[model_providers.gatellm]
name = "GateLLM"
base_url = "http://localhost:7890/v1"
env_key = "GATELLM_API_KEY"
wire_api = "responses"
```

```bash
export GATELLM_API_KEY=<gateway access key>
codex
```

**The one trap:** `wire_api`. If your upstream model only speaks Chat Completions, switch
this to `chat` — leaving it on `responses` sends requests the upstream cannot answer.

Full walkthrough: <https://docs.gatellm.io/en/reference/clients-and-gateway-diffs>
