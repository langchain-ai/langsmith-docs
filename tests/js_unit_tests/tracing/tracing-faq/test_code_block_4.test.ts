import { ChatOpenAI } from "langchain/chat_models/openai";
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
} from "langchain/prompts";

test("test_code_block_4", async () => {
  const chatPrompt = ChatPromptTemplate.fromPromptMessages([
    HumanMessagePromptTemplate.fromTemplate("{query}"),
  ]);

  const chain = chatPrompt.pipe(new ChatOpenAI());
  const configuredChain = chain.withConfig({ runName: "MyCustomChain" });
  await configuredChain.invoke({ query: "What is the meaning of life?" });
});
