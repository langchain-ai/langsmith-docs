import { ChatOpenAI } from "langchain/chat_models/openai";
import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";

test('test_code_block_4', async () => {
    const chatModel = new ChatOpenAI();
    const chain = new LLMChain({
      llm: chatModel,
      prompt: PromptTemplate.fromTemplate("What's the answer to {input}?"),
    });
    
    await chain.invoke(
      { input: "What is the meaning of life?" },
      { metadata: { variant: "abc123" } }
    );
});
