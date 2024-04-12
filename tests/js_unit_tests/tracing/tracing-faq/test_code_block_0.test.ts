import { ChatAnthropic } from "langchain/chat_models/anthropic";

test("test_code_block_0", async () => {
  const llm = new ChatAnthropic();
  await llm.invoke("Hello, World!");
});
