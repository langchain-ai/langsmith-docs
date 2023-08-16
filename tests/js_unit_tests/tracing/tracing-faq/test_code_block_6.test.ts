import { CallbackManager, traceAsGroup, TraceGroup } from "langchain/callbacks";
import { LLMChain } from "langchain/chains";
import { ChatOpenAI } from "langchain/chat_models/openai";
import { PromptTemplate } from "langchain/prompts";

test('test_code_block_6', async () => {
    // Initialize the LLMChain
    const llm = new ChatOpenAI({ temperature: 0.9 });
    const prompt = new PromptTemplate({
      inputVariables: ["question"],
      template: "What is the answer to {question}?",
    });
    const chain = new LLMChain({ llm, prompt });
    // You can group runs together using the traceAsGroup function
    const blockResult = await traceAsGroup(
      { name: "my_group_name" },
      async (manager: CallbackManager, questions: string[]) => {
        await chain.invoke({ question: questions[0] }, { callbacks: manager });
        await chain.invoke({ question: questions[1] }, { callbacks: manager });
        const finalResult = await chain.invoke(
          { question: questions[2] },
          { callbacks: manager }
        );
        return finalResult;
      },
      ["What is your name?", "What is your quest?", "What is your favorite color?"]
    );
    console.log(blockResult);
    
    // Or you can manually control the start and end of the grouped run
    const traceGroup = new TraceGroup("my_group_name");
    const groupManager = await traceGroup.start();
    try {
      await chain.invoke({ question: "What is your name?" }, { callbacks: groupManager });
      await chain.invoke({ question: "What is your quest?" }, { callbacks: groupManager });
      await chain.invoke(
        { question: "What is the airspeed velocity of an unladen swallow?" },
        { callbacks: groupManager }
      );
    } finally {
      // Code goes here
      await traceGroup.end();
    }
});
