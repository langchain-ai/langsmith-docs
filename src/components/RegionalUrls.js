import React, { useState, useEffect } from "react";

export const RegionalUrl = () => {
  const [url, setUrl] = useState("https://smith.langchain.com");

  useEffect(() => {
    const storedUrl = localStorage.getItem('ls:docs:langsmithUrl') || 'https://smith.langchain.com';
    setUrl(storedUrl);
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
