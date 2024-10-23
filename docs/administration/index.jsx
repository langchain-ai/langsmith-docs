import React, { useEffect } from "react";
import { useHistory } from "@docusaurus/router";

export default function Home() {
  const history = useHistory();

  useEffect(() => {
    // Redirect to the subdirectory '/docs'
    history.push("/docs");
  }, [history]);

  return null; // Return nothing because we're redirecting
}
