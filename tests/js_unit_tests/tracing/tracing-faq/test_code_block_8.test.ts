import { Client } from "langsmith";
import { LangChainTracer } from "langchain/callbacks";
import { ChatOpenAI } from "langchain/chat_models/openai";

test('test_code_block_8', async () => {
    const llm = new ChatOpenAI({
      callbacks: [
        new LangChainTracer({
          projectName: "YOUR_PROJECT_NAME_HERE",
          client: new Client({
            apiUrl: "https://api.smith.langchain.com",
            apiKey: "YOUR_API_KEY_HERE",
          }),
        }),
      ],
    });
    await llm.invoke("Hello, world!");
});
