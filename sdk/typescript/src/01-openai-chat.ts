// OpenAI SDK — one chat completion, pointed at the gateway.
//
//   npm run 01
//
// Only `baseURL` and `apiKey` change. Everything after that is ordinary OpenAI SDK code.

import OpenAI from 'openai';

import { MODEL, OPENAI_BASE_URL, requireKey } from './common.js';

const client = new OpenAI({ baseURL: OPENAI_BASE_URL, apiKey: requireKey() });

const response = await client.chat.completions.create({
  model: MODEL,
  messages: [{ role: 'user', content: 'In one sentence, what is an AI gateway?' }],
});

console.log(response.choices[0]?.message.content);
console.log(`model: ${response.model} | tokens: ${response.usage?.total_tokens}`);
