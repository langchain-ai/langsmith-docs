import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";

export function TypeScriptBlock(content) {
  return {
    value: "typescript",
    label: "Typescript",
    content: content,
  };
}

export function PythonBlock(content) {
  return {
    value: "python",
    label: "Python",
    content: content,
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
