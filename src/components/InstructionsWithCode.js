import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";
import Markdown from "react-markdown";

export function LangChainPyBlock(content) {
  return {
    value: "langchain-py",
    label: "LangChain (Python)",
    content,
    language: "python",
  };
}

export function LangChainJSBlock(content) {
  return {
    value: "langchain-js",
    label: "LangChain (JS)",
    content,
    language: "typescript",
  };
}

export function TypeScriptBlock(content, caption = "") {
  return {
    value: "typescript",
    label: "TypeScript SDK",
    content,
    caption,
    language: "typescript",
  };
}

export function PythonBlock(content, caption = "") {
  return {
    value: "python",
    label: "Python SDK",
    content,
    caption,
    language: "python",
  };
}

export function APIBlock(content, caption = "") {
  return {
    value: "api",
    label: "API (Using Python Requests)",
    content,
    caption,
    language: "python",
  };
}

export function ShellBlock(content, value = "shell", label = "Shell") {
  return {
    value,
    label,
    content,
  };
}

export function CodeTabs({ tabs, groupId }) {
  return (
    <Tabs groupId={groupId}>
      {tabs.map((tab, index) => {
        const key = `${groupId}-${index}`;
        return (
          <TabItem key={key} value={tab.value} label={tab.label}>
            {tab.caption && <Markdown>{tab.caption}</Markdown>}
            <CodeBlock
              className={tab.value}
              language={tab.language ?? tab.value}
            >
              {tab.content}
            </CodeBlock>
          </TabItem>
        );
      })}
    </Tabs>
  );
}
