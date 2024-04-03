import React from 'react';
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from '@theme/CodeBlock';

import {
  CodeTabs,
  PythonBlock,
  TypeScriptBlock,
  ShellBlock,
} from './InstructionsWithCode';

export const HubInstallationCodeTabs = () => (
  <CodeTabs
    groupId="client-language"
    tabs={[
      {
        value: 'python',
        label: 'pip',
        language: 'bash',
        content: `pip install -U langchain langchainhub`,
      },
      {
        value: 'typescript',
        label: 'yarn',
        language: 'bash',
        content: `yarn add langchain`,
      },
      {
        value: 'npm',
        label: 'npm',
        language: 'bash',
        content: `npm install -S langchain`,
      },
      {
        value: 'pnpm',
        label: 'pnpm',
        language: 'bash',
        content: `pnpm add langchain`,
      },
    ]}
  />
);

export const HubPullCodeTabs = ({}) => {
  const pyBlock = `from langchain import hub

# pull a chat prompt
prompt = hub.pull("efriis/my-first-prompt")

# create a model to use it with
from langchain.chat_models import ChatOpenAI
model = ChatOpenAI()

# use it in a runnable
runnable = prompt | model
runnable.invoke({
	"profession": "biologist",
	"question": "What is special about parrots?",
})`;

const jsBlock = `// import
import * as hub from "langchain/hub";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { ChatOpenAI } from "langchain/chat_models/openai";

// pull a chat prompt
await hub.pull<ChatPromptTemplate>("efriis/my-first-prompt");


// create a model to use it with
const model = new ChatOpenAI();

// use it in a runnable
const runnable = prompt.pipe(model);
const result = await runnable.invoke({
  "profession": "biologist",
  "question": "What is special about parrots?",
});

console.log(result);`

  return (
    <Tabs groupId="client-language">
      <TabItem key="python" value="python" label="Python">
        <CodeBlock className="python" language="python">
          {pyBlock}
        </CodeBlock>
      </TabItem>
      <TabItem key="typescript" value="typescript" label="TypeScript">
        <CodeBlock className="typescript" language="typescript">
          {jsBlock}
        </CodeBlock>
      </TabItem>
    </Tabs>
  );
};

export const HubPushCodeTabs = ({}) => {
  const pyBlock = `from langchain import hub
from langchain.prompts.chat import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

hub.push("<handle>/topic-joke-generator", prompt)`;

const jsBlock = `import * as hub from "langchain/hub";
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
} from 'langchain/prompts';

const message = HumanMessagePromptTemplate.fromTemplate(
  'tell me a joke about {topic}'
);
const prompt = ChatPromptTemplate.fromPromptMessages([message]);

await hub.push("<handle>/my-first-prompt", prompt);`

  return (
    <Tabs groupId="client-language">
      <TabItem key="python" value="python" label="Python">
        <CodeBlock className="python" language="python">
          {pyBlock}
        </CodeBlock>
      </TabItem>
      <TabItem key="typescript" value="typescript" label="TypeScript">
        <CodeBlock className="typescript" language="typescript">
          {jsBlock}
        </CodeBlock>
      </TabItem>
    </Tabs>
  );
};