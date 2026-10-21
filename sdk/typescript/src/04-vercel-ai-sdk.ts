// Vercel AI SDK — createAnthropic against the gateway.
//
//   npm run 04
//
// `createAnthropic` appends `/messages`, so its baseURL must include `/v1` — the reverse
// of the Anthropic SDK, which appends `/v1/messages` and takes the bare root.

import { createAnthropic } from '@ai-sdk/anthropic';
import { generateText } from 'ai';

import { MODEL, VERCEL_ANTHROPIC_BASE_URL, requireKey } from './common.js';

const anthropic = createAnthropic({
  baseURL: VERCEL_ANTHROPIC_BASE_URL,
  apiKey: requireKey(),
});

const { text, usage } = await generateText({
  model: anthropic(MODEL),
  prompt: 'In one sentence, what does an LLM gateway meter?',
});

console.log(text);
console.log(`tokens: ${usage?.totalTokens}`);
