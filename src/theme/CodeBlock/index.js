/* eslint-disable react/jsx-props-no-spreading */
import React, { useState } from "react";
import CodeBlock from "@theme-original/CodeBlock";

function Imports({ imports }) {
  return (
    <div
      style={{
        paddingTop: "1.3rem",
        background: "var(--prism-background-color)",
        color: "var(--prism-color)",
        marginTop: "calc(-1 * var(--ifm-leading) - 5px)",
        marginBottom: "var(--ifm-leading)",
        boxShadow: "var(--ifm-global-shadow-lw)",
        borderBottomLeftRadius: "var(--ifm-code-border-radius)",
        borderBottomRightRadius: "var(--ifm-code-border-radius)",
      }}
    >
      <h4 style={{ paddingLeft: "0.65rem", marginBottom: "0.45rem" }}>
        API Reference:
      </h4>
      <ul style={{ paddingBottom: "1rem" }}>
        {imports.map(({ imported, source, docs }) => (
          <li>
            <a href={docs}>
              <span>{imported}</span>
            </a>{" "}
            from <code>{source}</code>
          </li>
        ))}
      </ul>
    </div>
  );
}

function CollapsibleCodeBlock({ children, ...props }) {
  const processCode = (code) => {
    const lines = code.split("\n");
    const processedLines = [];
    let currentSection = null;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Check for region with optional [collapsed] flag
      const regionMatch = line.match(
        /(\/\/#region|#region)\s*(\[collapsed\])?\s*(.*)/
      );
      if (regionMatch) {
        currentSection = {
          start: i,
          title: regionMatch[3].trim(),
          content: [],
          defaultCollapsed: !!regionMatch[2], // true if [collapsed] is present
        };
      } else if (line.includes("#endregion") || line.includes("//#endregion")) {
        if (currentSection) {
          processedLines.push({
            type: "section",
            ...currentSection,
            end: i,
          });
          currentSection = null;
        }
      } else if (currentSection) {
        currentSection.content.push(line);
      } else {
        processedLines.push({ type: "line", content: line });
      }
    }

    return processedLines;
  };

  const toggleSection = (index) => {
    const newCollapsed = new Set(collapsedSections);
    if (newCollapsed.has(index)) {
      newCollapsed.delete(index);
    } else {
      newCollapsed.add(index);
    }
    setCollapsedSections(newCollapsed);
  };

  const [collapsedSections, setCollapsedSections] = useState(() => {
    const initial = new Set();
    if (typeof children === "string") {
      const processed = processCode(children);
      processed.forEach((item, index) => {
        if (item.type === "section" && item.defaultCollapsed) {
          initial.add(index);
        }
      });
    }
    return initial;
  });

  const renderCode = () => {
    if (typeof children !== "string") {
      return children;
    }

    const processedCode = processCode(children);
    let result = "";

    processedCode.forEach((item, index) => {
      if (item.type === "line") {
        result += item.content + "\n";
      } else {
        const isCollapsed = collapsedSections.has(index);
        // Always show the first line
        result += item.content[0] + (isCollapsed ? " ...\n" : "\n");
        if (!isCollapsed) {
          // Add the rest of the content starting from the second line
          result +=
            item.content.slice(1).join("\n") +
            (index < processedCode.length - 1 ? "\n" : ""); // Only add newline if not last item
        }
      }
    });

    return result.trimEnd(); // Remove trailing whitespace and newlines
  };

  const getGutterItems = () => {
    if (typeof children !== "string") return [];

    const processedCode = processCode(children);
    const items = [];
    let lineCount = 0;

    processedCode.forEach((item, index) => {
      if (item.type === "line") {
        lineCount++;
      } else {
        const isCollapsed = collapsedSections.has(index);
        items.push({
          line: lineCount,
          title: item.title,
          isCollapsed,
          index,
        });
        // Always count the first line
        lineCount += 1;
        if (!isCollapsed) {
          // Add the remaining lines if not collapsed
          lineCount += item.content.slice(1).length;
        }
      }
    });

    return items;
  };

  React.useEffect(() => {
    const style = document.createElement("style");
    style.textContent = `
    .code-block-wrapper {
      position: relative;
    }

    `;
    document.head.appendChild(style);
    return () => document.head.removeChild(style);
  }, []);

  const gutterItems = getGutterItems();
  const codeContent = renderCode();

  return (
    <div className="code-block-wrapper">
      <div className="fold-markers">
        {gutterItems.map((item) => (
          <div
            key={item.index}
            className={`fold-marker ${item.isCollapsed ? "collapsed" : ""}`}
            onClick={() => toggleSection(item.index)}
            style={{
              top: `${item.line * 22.0375}px`, // Back to using fixed pixel height
            }}
          >
            ⌵
          </div>
        ))}
      </div>
      <div className="code-block-with-gutter">
        <CodeBlock {...props}>{codeContent}</CodeBlock>
      </div>
    </div>
  );
}

export default function CodeBlockWrapper({ children, ...props }) {
  if (typeof children === "string") {
    return <CollapsibleCodeBlock {...props}>{children}</CollapsibleCodeBlock>;
  }

  return (
    <>
      <CollapsibleCodeBlock {...props}>{children.content}</CollapsibleCodeBlock>
      {children.imports && <Imports imports={children.imports} />}
    </>
  );
}
