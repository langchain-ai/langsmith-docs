import React, { useState, useEffect } from "react";
import CodeBlock from "@theme/CodeBlock";

const DOMAINS = {
  US: {
    langsmith: "smith.langchain.com",
    api: "api.smith.langchain.com",
    hub: "api.hub.langchain.com",
  },
  EU: {
    langsmith: "eu.smith.langchain.com",
    api: "eu.api.smith.langchain.com",
    hub: "eu.api.hub.langchain.com",
  },
};

export function RegionalUrl({
  text,
  type = "langsmith",
  suffix = "",
  link = "true",
}) {
  const [domains, setDomains] = useState(DOMAINS.US);

  useEffect(() => {
    const storedRegion =
      localStorage.getItem("ls:docs:langsmithRegion") || "US";
    setDomains(DOMAINS[storedRegion]);
    const handleStorageChange = () => {
      setDomains(
        DOMAINS[localStorage.getItem("ls:docs:langsmithRegion") || "US"]
      );
    };

    window.addEventListener("storage", handleStorageChange);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  const domain = domains[type];
  const resolvedUrl = `https://${domain}${suffix}`;
  if (link === "true") {
    return <a href={resolvedUrl}>{text || resolvedUrl}</a>;
  }

  return <code>{resolvedUrl}</code>;
}
