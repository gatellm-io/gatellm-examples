# Claude Code

Claude Code speaks the Anthropic protocol and reads its endpoint from environment
variables. Point it at the gateway root — it appends `/v1/messages` itself.

```bash
export ANTHROPIC_BASE_URL=http://localhost:7890
export ANTHROPIC_API_KEY=<gateway access key>
export ANTHROPIC_MODEL=<model your gateway exposes>
```

Then start `claude` as usual.

**The one trap:** Claude Code pins its own model ids. If it asks for a model your gateway
does not expose under that exact name, the request fails. Either configure the gateway
with the same name, or set `ANTHROPIC_MODEL` to the gateway name.

Full walkthrough: <https://docs.gatellm.io/en/quickstart/claude-code-via-gateway>
