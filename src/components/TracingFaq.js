import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";

export const AccessRunIdBlock = ({}) => {
  const callbackPythonBlock = `from langchain import chat_models, prompts, callbacks
chain = (
    prompts.ChatPromptTemplate.from_template("Say hi to {name}")
    | chat_models.ChatOpenAI()
)
with callbacks.collect_runs() as cb:
  result = chain.invoke({"name": "Clara"})
  run_id = id.traced_runs[0].id
print(run_id)
`;

  const alternativePythonBlock = `from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain\n
chain = LLMChain.from_string(ChatOpenAI(), "Say hi to {name}")
response = chain("Clara", include_run_info=True)
run_id = response["__run"].run_id
print(run_id)`;

  const chatModelPythonBlock = `from langchain.chat_models import ChatOpenAI
 from langchain.prompts import ChatPromptTemplate
 
 chat_model = ChatOpenAI()
 
 prompt = ChatPromptTemplate.from_messages(
     [
         ("system", "You are a cat"),
         ("human", "Hi"),
     ]
 )
 res = chat_model.generate(messages=[prompt.format_messages()])
 res.run[0].run_id`;

  const llmModelPythonBlock = `python
 from langchain.llms import OpenAI

openai = OpenAI()
res = openai.generate(["You are a good bot"])
print(res.run[0].run_id)`;
  return (
    <Tabs groupId="client-language">
      <TabItem key="python" value="python" label="Python">
        <CodeBlock className="python" language="python">
          {callbackPythonBlock}
        </CodeBlock>
        <p>
          For older versions of LangChain ({`<`}0.0.276), you can instruct the
          chain to return the run ID by specifying the `include_run_info=True`
          parameter to the call function:
        </p>
        <CodeBlock className="python" language="python">
          {alternativePythonBlock}
        </CodeBlock>
        <p>
          For python LLMs/chat models, the run information is returned
          automatically when calling the `generate()` method. Example:
        </p>
        <CodeBlock className="python" language="python">
          {chatModelPythonBlock}
        </CodeBlock>
        <p>or for LLMs</p>
        <CodeBlock className="python" language="python">
          {llmModelPythonBlock}
        </CodeBlock>
      </TabItem>
      <TabItem key="typescript" value="typescript" label="TypeScript">
        <CodeBlock className="typescript" language="typescript">
          {`import { ChatOpenAI } from "langchain/chat_models/openai";
import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";\n
const prompt = PromptTemplate.fromTemplate("Say hi to {name}");
const chain = new LLMChain({
  llm: new ChatOpenAI(),
  prompt: prompt,
});\n
const response = await chain.invoke({ name: "Clara" });
console.log(response.__run);`}
        </CodeBlock>
      </TabItem>
    </Tabs>
  );
};
