/** Basic chat completion example. */
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://dubhehub.com/v1"
});

const response = await client.chat.completions.create({
  model: "dubhe-fast",
  messages: [
    { role: "user", content: "What is the capital of Japan?" }
  ]
});
console.log(response.choices[0].message.content);
