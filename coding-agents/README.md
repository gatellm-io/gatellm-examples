# Coding agents

Terminal agents that can be pointed at a custom endpoint. Each folder records only the
config file and the variable names — the stable part. The full walkthrough for each one
lives in the docs.

| Agent | Speaks | Config | Key variables |
|---|---|---|---|
| [Claude Code](claude-code/README.md) | Anthropic | env vars | `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` |
| [Codex CLI](codex-cli/README.md) | OpenAI Responses | `~/.codex/config.toml` | `base_url`, `env_key`, `wire_api` |
| [Gemini CLI](gemini-cli/README.md) | Gemini | env vars | `GOOGLE_GEMINI_BASE_URL`, `GEMINI_API_KEY` |

The full list of supported agents — including the ones that cannot be pointed at a custom
endpoint — is at <https://gatellm.io/coding-agents>.
