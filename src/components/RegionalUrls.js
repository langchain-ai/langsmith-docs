import React, { useState, useEffect } from "react";
import ExecutionEnvironment from "@docusaurus/ExecutionEnvironment";

export const RegionalUrl = () => {
  var url;
  var setUrl;
  if (ExecutionEnvironment.canUseDOM) {
    [url, setUrl] = useState(
      localStorage.getItem("ls:docs:langsmithUrl") ||
        "https://smith.langchain.com"
    );
  } else {
    [url, setUrl] = useState("https://smith.langchain.com");
  }

  useEffect(() => {
    const handleStorageChange = () => {
      setUrl(
        localStorage.getItem("ls:docs:langsmithUrl") ||
          "https://smith.langchain.com"
      );
    };

    window.addEventListener("storage", handleStorageChange);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  return <a href={url}>{url}</a>;
};
