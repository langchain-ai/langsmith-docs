import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";

export function LangChainPyBlock(content) {
  return {
    value: "langchain-py",
    label: "LangChain (Python)",
    content: content,
    language: "python"
  };
}

export function LangChainJSBlock(content) {
  return {
    value: "langchain-js",
    label: "LangChain (JS)",
    content: content,
    language: "typescript"
  };
}


export function TypeScriptBlock(content) {
  return {
    value: "typescript",
    label: "TypeScript SDK",
    content: content,
    language: "typescript"
  };
}

export function PythonBlock(content) {
  return {
    value: "python",
    label: "Python SDK",
    content: content,
    language: "python"
  };
}

export function APIBlock(content) {
  return {
    value: "api",
    label: "API (Using Python Requests)",
    content: content,
    language: "python"
  };
}

export function ShellBlock(content, value = "shell", label = "Shell") {
  return {
    value: value,
    label: label,
    content: content,
  };
}

export const CodeTabs = ({ tabs, groupId }) => (
  <Tabs groupId={groupId}>
    {tabs.map((tab, index) => (
      <TabItem key={index} value={tab.value} label={tab.label}>
        <CodeBlock className={tab.value} language={tab.language ?? tab.value}>
          {tab.content}
        </CodeBlock>
      </TabItem>
    ))}
  </Tabs>
);
