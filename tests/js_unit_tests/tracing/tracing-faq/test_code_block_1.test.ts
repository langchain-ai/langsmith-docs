import { ChatOpenAI } from "langchain/chat_models/openai";
import {  ChatPromptTemplate,
  HumanMessagePromptTemplate,
} from "langchain/prompts";

import { LangChainTracer } from "langchain/callbacks";

test('test_code_block_1', async () => {
    const chatPrompt = ChatPromptTemplate.fromPromptMessages([
      HumanMessagePromptTemplate.fromTemplate("{query}"),
    ]);
    
    const chain = chatPrompt.pipe(new ChatOpenAI());
    
    const tracer = new LangChainTracer({ projectName: "My Project" });
    await chain.invoke({
      query: "How many people live in canada as of 2023?" },
      { callbacks: [tracer]
    });
});
