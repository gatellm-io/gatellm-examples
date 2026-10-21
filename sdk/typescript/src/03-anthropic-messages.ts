// Anthropic SDK — Messages API.
//
//   npm run 03
//
// Note the base URL: the Anthropic SDK appends `/v1/messages` itself, so pass the gateway
// root, not `<root>/v1` — the opposite of the OpenAI SDK.

import Anthropic from '@anthropic-ai/sdk';

import { ANTHROPIC_BASE_URL, MODEL, requireKey } from './common.js';

const client = new Anthropic({ baseURL: ANTHROPIC_BASE_URL, apiKey: requireKey() });

const message = await client.messages.create({
  model: MODEL,
  max_tokens: 512,
  messages: [{ role: 'user', content: 'In one sentence, what does a gateway do?' }],
});

// Thinking blocks can come back before the text block, so take the first text block
// rather than assuming content[0] is the answer.
const text = message.content.find((block) => block.type === 'text');
console.log(text && 'text' in text ? text.text : '(no text block)');
