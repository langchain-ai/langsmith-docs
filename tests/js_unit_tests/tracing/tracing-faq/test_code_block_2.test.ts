import { PromptTemplate } from "langchain/prompts";
import { ChatOpenAI } from "langchain/chat_models/openai";

test("test_code_block_2", async () => {
  const llm = new ChatOpenAI({ temperature: 0, tags: ["my-llm-tag"] });
  const prompt = PromptTemplate.fromTemplate("Say {input}");
  const chain = prompt
    .pipe(llm)
    .withConfig({ tags: ["my-bash-tag", "another-tag"] });

  await chain.invoke({ input: "Hello, World!" }, { tags: ["shared-tags"] });
});
