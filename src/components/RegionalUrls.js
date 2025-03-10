import React, { useState, useEffect } from "react";
import CodeBlock from "@theme/CodeBlock";

const DOMAINS = {
  US: {
    auth: "auth.langchain.com",
    langsmith: "smith.langchain.com",
    api: "api.smith.langchain.com",
    hub: "api.smith.langchain.com",
  },
  EU: {
    auth: "eu.auth.langchain.com",
    langsmith: "eu.smith.langchain.com",
    api: "eu.api.smith.langchain.com",
    hub: "eu.api.smith.langchain.com",
  },
};

export function RegionalUrl({
  text,
  type = "langsmith",
  suffix = "",
  link = true,
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
  if (link) {
    return <a href={resolvedUrl}>{text || resolvedUrl}</a>;
  }

  return <code>{resolvedUrl}</code>;
}
