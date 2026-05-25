/** Vision (image understanding) example. Requires dubhe-vision model. */
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://dubhehub.com/v1"
});

const response = await client.chat.completions.create({
  model: "dubhe-vision",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        {
          type: "image_url",
          image_url: {
            url: "https://example.com/photo.jpg"
          }
        }
      ]
    }
  ]
});
console.log(response.choices[0].message.content);
