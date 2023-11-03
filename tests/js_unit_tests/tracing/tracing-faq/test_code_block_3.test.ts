import { ChatOpenAI } from "langchain/chat_models/openai";
import { ChatPromptTemplate } from "langchain/prompts";

test('test_code_block_3', async () => {
    const chatModel = new ChatOpenAI();
    const prompt = ChatPromptTemplate.fromMessages([
      ["system", "You are a helpful AI."],
      ["human", "{input}"],
    ]);
    const chain = prompt.pipe(chatModel);
    
    await chain.invoke(
      { input: "What is the meaning of life?" },
      { metadata: { myKey: "My Value" } }
    );
});
