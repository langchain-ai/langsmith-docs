import React from 'react';
import CodeBlock from '@theme/CodeBlock';
import {
  CodeTabs,
  PythonBlock,
  TypeScriptBlock,
  ShellBlock,
} from './InstructionsWithCode';

export const LangChainInstallationCodeTabs = () => (
  <CodeTabs
    groupId="client-language"
    tabs={[
      {
        value: 'python',
        label: 'pip',
        language: 'bash',
        content: `pip install -U langchain`,
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

export const ConfigureEnvironmentCodeTabs = ({}) => (
  <CodeTabs
    tabs={[
      ShellBlock(`export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"`),
    ]}
    groupId="client-language"
  />
);

export const LangChainQuickStartCodeTabs = ({}) => (
  <CodeTabs
    tabs={[
      PythonBlock(`from langchain.chat_models import ChatOpenAI\n
llm = ChatOpenAI()
llm.predict("Hello, world!")`),
      TypeScriptBlock(`import { ChatOpenAI } from "langchain/chat_models/openai";\n
const llm = new ChatOpenAI()
await llm.predict("Hello, world!");

/**
 * For environments where process.env is not defined,
 * initialize by explicitly passing keys:
 */

import { Client } from "langsmith";
import { LangChainTracer } from "langchain/callbacks";

const client = new Client({
  apiUrl: "https://api.smith.langchain.com",
  apiKey: "YOUR_API_KEY"
});

const tracer = new LangChainTracer({
  projectName: "YOUR_PROJECT_NAME",
  client
});

const model = new ChatOpenAI({
  openAIApiKey: "YOUR_OPENAI_API_KEY",
  callbacks: [tracer]
});`),
    ]}
    groupId="client-language"
  />
);

const TraceableQuickStart = {
  value: 'python-experimental',
  language: `python`,
  label: 'Python (experimental)',
  content: `import datetime
from typing import Any\n
import openai
from langsmith.run_helpers import traceable


@traceable(run_type="llm")
def my_llm(prompt: str, temperature: float = 0.0, **kwargs: Any) -> str:
  messages = [
      {
          "role": "system",
          "content": "You are an AI Assistant. The time is "
          + str(datetime.datetime.now()),
      },
      {"role": "user", "content": prompt},
  ]
  return (
      openai.ChatCompletion.create(
          model="gpt-3.5-turbo", messages=messages, temperature=temperature, **kwargs
      )
      .choices[0]
      .message.content
  )


@traceable(run_type="tool")
def my_tool(tool_input: str) -> str:
  return tool_input.upper()


@traceable(run_type="chain")
def my_chat_bot(text: str) -> str:
  generated = my_llm(text, temperature=0.0)

  if "meeting" in generated:
    return my_tool(generated)
  else:
    return generated\n\n
my_chat_bot("Summarize this morning's meetings.")
# See an example run at: https://smith.langchain.com/public/b5e2666d-f570-4b83-a611-86a2503ed91b/r`,
};

export const TraceableQuickStartCodeBlock = ({}) => (
  <CodeBlock
    className={TraceableQuickStart.value}
    language={TraceableQuickStart.language}
  >
    {TraceableQuickStart.content}
  </CodeBlock>
);

export const TraceableThreadingCodeBlock = ({}) => (
  <CodeBlock
    className={TraceableQuickStart.value}
    language={TraceableQuickStart.language}
  >
    {`import asyncio
import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import Any\n
import openai
from langsmith.run_helpers import traceable
from langsmith.run_trees import RunTree\n\n
@traceable(run_type="llm")
def my_llm(prompt: str, temperature: float = 0.0, **kwargs: Any) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are an AI Assistant. The time is "
            + str(datetime.datetime.now()),
        },
        {"role": "user", "content": prompt},
    ]
    return (
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=temperature, **kwargs
        )
        .choices[0]
        .message.content
    )\n\n
@traceable(run_type="chain")
# highlight-next-line
async def nested_chain(text: str, run_tree: RunTree, **kwargs: Any) -> str:
    thread_pool = ThreadPoolExecutor(max_workers=1)
    futures = []
    for i in range(2):
        futures.append(
            thread_pool.submit(
                my_llm,
                f"Gather {i}: {text}",
                # highlight-next-line
                langsmith_extra={"run_tree": run_tree},
                **kwargs,
            )
        )
    thread_pool.shutdown(wait=True)
    results = [future.result() for future in futures]
    return "\\n".join(results)\n\n
    await nested_chain("Summarize meeting")`}
  </CodeBlock>
);

export const RunTreeQuickStartCodeTabs = ({}) => (
  <CodeTabs
    tabs={[
      PythonBlock(`from langsmith.run_trees import RunTree\n
parent_run = RunTree(
    name="My Chat Bot",
    run_type="chain",
    inputs={"text": "Summarize this morning's meetings."},
    serialized={}
)\n
child_llm_run = parent_run.create_child(
    name="My Proprietary LLM",
    run_type="llm",
    inputs={
        "prompts": [
            "You are an AI Assistant. Summarize this morning's meetings."
        ]
    },
)\n
child_llm_run.end(outputs={"generations": ["Summary of the meeting..."]})
parent_run.end(outputs={"output": ["The meeting notes are as follows:..."]})\n
res = parent_run.post(exclude_child_runs=False)
res.result()`),
      TraceableQuickStart,
      TypeScriptBlock(`import { RunTree, RunTreeConfig } from "langsmith";\n
const parentRunConfig: RunTreeConfig = {
    name: "My Chat Bot",
    run_type: "chain",
    inputs: {
        text: "Summarize this morning's meetings.",
    },
    serialized: {}
};\n
const parentRun = new RunTree(parentRunConfig);\n
const childLlmRun = await parentRun.createChild({
    name: "My Proprietary LLM",
    run_type: "llm",
    inputs: {
        prompts: [
        "You are an AI Assistant. Summarize this morning's meetings.",
        ],
    },
});\n
await childLlmRun.end({
outputs: {
    generations: [
    "Summary of the meeting...",
    ],
},
});\n
await parentRun.end({
outputs: {
    output: ["The meeting notes are as follows:..."],
},
});\n
// False means post all nested runs as a batch
// (don't exclude child runs)
await parentRun.postRun(false);

  `),
    ]}
    groupId="client-language"
  />
);
