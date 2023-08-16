import { ChatOpenAI } from "langchain/chat_models/openai";
import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";

test('test_code_block_7', async () => {
    const prompt = PromptTemplate.fromTemplate("Say hi to {name}");
    const chain = new LLMChain({
      llm: new ChatOpenAI(),
      prompt: prompt,
    });
    
    async function main() {
      const response = await chain.invoke({ name: "Clara" });
      console.log(response.__run);
    }
    
    main();
});
