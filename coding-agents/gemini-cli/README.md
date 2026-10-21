# Gemini CLI

Gemini CLI reads its endpoint from environment variables and speaks the Gemini protocol.

```bash
export GOOGLE_GEMINI_BASE_URL=http://localhost:7890
export GEMINI_API_KEY=<gateway access key>
```

Then start `gemini` as usual.

**The one trap:** Gemini CLI can authenticate with a Google account (OAuth) instead of an
API key. Mixed modes send the wrong credential to the gateway — use the key mode, not the
OAuth login, when the endpoint is your own gateway.

Full walkthrough: <https://docs.gatellm.io/en/reference/clients-and-gateway-diffs>
