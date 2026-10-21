// OpenAI SDK — streaming.
//
//   npm run 02

import OpenAI from 'openai';

import { MODEL, OPENAI_BASE_URL, requireKey } from './common.js';

const client = new OpenAI({ baseURL: OPENAI_BASE_URL, apiKey: requireKey() });

const stream = await client.chat.completions.create({
  model: MODEL,
  messages: [{ role: 'user', content: 'Count from 1 to 20, one number per line.' }],
  stream: true,
});

for await (const chunk of stream) {
  const delta = chunk.choices[0]?.delta?.content;
  if (delta) process.stdout.write(delta);
}

process.stdout.write('\n');
