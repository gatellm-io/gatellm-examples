// Shared configuration for the TypeScript examples.
// This is the only place that knows the per-protocol path convention.

export const BASE_URL = (process.env.GATELLM_BASE_URL ?? 'http://localhost:7890').replace(/\/+$/, '');
export const API_KEY = process.env.GATELLM_API_KEY ?? '';
export const MODEL = process.env.GATELLM_MODEL ?? 'claude-opus-5';

// OpenAI-style clients append /chat/completions, /responses, /embeddings, ...
export const OPENAI_BASE_URL = `${BASE_URL}/v1`;
// Anthropic clients append /v1/messages themselves, so the root is correct.
export const ANTHROPIC_BASE_URL = BASE_URL;
// Vercel AI SDK's createAnthropic appends /messages — the reverse of the Anthropic SDK.
export const VERCEL_ANTHROPIC_BASE_URL = `${BASE_URL}/v1`;

export function requireKey(): string {
  if (!API_KEY) {
    throw new Error(
      'GATELLM_API_KEY is not set. Create an access key in the console ' +
        '(http://localhost:7890) and export it, or copy ../.env.example to ../.env.',
    );
  }
  return API_KEY;
}
