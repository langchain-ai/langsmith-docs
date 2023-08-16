import { ChatOpenAI } from "langchain/chat_models/openai";
import { awaitAllCallbacks } from "langchain/callbacks";

test('test_code_block_9', async () => {
    const llm = new ChatOpenAI();
    llm.invoke("Hello, World!").finally(() => awaitAllCallbacks());
});
