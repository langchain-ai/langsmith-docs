import { ChatOpenAI } from "langchain/chat_models/openai";
import { Client } from "langsmith";
import { LangChainTracer } from "langchain/callbacks";

test('test_code_block_7', async () => {
    const callbacks = [
      new LangChainTracer({
        projectName: "YOUR_PROJECT_NAME_HERE",
        client: new Client({
          apiUrl: "https://api.smith.langchain.com",
          apiKey: "YOUR_API_KEY_HERE",
        }),
      }),
    ];
    const llm = new ChatOpenAI({});
    await llm.invoke("Hello, world!", { callbacks });
});
