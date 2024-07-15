import React, { useState, useEffect } from "react";

const DOMAINS = {
  US: {
    langsmith: "smith.langchain.com",
    api: "api.smith.langchain.com",
  },
  EU: {
    langsmith: "eu.smith.langchain.com",
    api: "eu.api.smith.langchain.com",
  },
};

export const RegionalUrl = ({ text, type = "langsmith", suffix = "" }) => {
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
  return <a href={resolvedUrl}>{text || resolvedUrl}</a>;
};
