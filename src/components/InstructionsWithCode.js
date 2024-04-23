import React from "react";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import CodeBlock from "@theme/CodeBlock";
import { marked } from "marked";
import DOMPurify from "isomorphic-dompurify";
import prettier from 'prettier';
import parserTypeScript from 'prettier/parser-typescript';

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

/**
 * 
 * @param {string} code 
 * @param {"typescript" | "python"} language 
 * @returns {string} The formatted code
 */
function formatCode(code, language) {
  language = language.toLowerCase();
  if (language === "python") {
    // no-op - Do not format Python code at this time
    return code;
  }

  try {
    const formattedCode = prettier.format(code, {
      parser: language,
      plugins: [parserTypeScript],
    });

    return formattedCode;
  } catch (_) {
    // no-op
  }
  // If formatting fails, return as is
  return code
}

export function CodeTabs({ tabs, groupId }) {
  return (
    <Tabs groupId={groupId}>
      {tabs.map((tab, index) => {
        const key = `${groupId}-${index}`;
        return (
          <TabItem key={key} value={tab.value} label={tab.label}>
            {tab.caption && (
              <div
                dangerouslySetInnerHTML={{
                  __html: DOMPurify.sanitize(marked.parse(tab.caption)),
                }}
              />
            )}
            <CodeBlock
              className={tab.value}
              language={tab.language ?? tab.value}
            >
              {formatCode(tab.content, tab.language ?? tab.value)}
            </CodeBlock>
          </TabItem>
        );
      })}
    </Tabs>
  );
}
