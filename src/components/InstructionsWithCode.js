import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";

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

export function TypeScriptBlock(content) {
  return {
    value: "typescript",
    label: "TypeScript SDK",
    content,
    language: "typescript",
  };
}

export function PythonBlock(content) {
  return {
    value: "python",
    label: "Python SDK",
    content,
    language: "python",
  };
}

export function APIBlock(content) {
  return {
    value: "api",
    label: "API (Using Python Requests)",
    content,
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
