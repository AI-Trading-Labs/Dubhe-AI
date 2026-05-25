/** Function calling example. */
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://dubhehub.com/v1"
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "Get the current weather for a city",
      parameters: {
        type: "object",
        properties: {
          city: { type: "string", description: "City name" },
          unit: { type: "string", enum: ["celsius", "fahrenheit"] }
        },
        required: ["city"]
      }
    }
  }
];

const response = await client.chat.completions.create({
  model: "dubhe-fast",
  messages: [{ role: "user", content: "What's the weather in Tokyo?" }],
  tools
});

const msg = response.choices[0].message;
if (msg.tool_calls) {
  for (const tc of msg.tool_calls) {
    console.log(`Call: ${tc.function.name}(${tc.function.arguments})`);
  }
}
