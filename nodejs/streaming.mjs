/** Streaming chat completion example. */
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://dubhehub.com/v1"
});

const stream = await client.chat.completions.create({
  model: "dubhe-fast",
  messages: [{ role: "user", content: "Write a short poem about AI." }],
  stream: true
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
