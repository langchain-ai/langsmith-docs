import React, { useState, useEffect } from "react";

const URLS = {
  US: "https://smith.langchain.com",
  EU: "https://eu.smith.langchain.com",
};

export default function RegionSelector() {
  const [selectedRegion, setSelectedRegion] = useState("US");

  useEffect(() => {
    const storedUrl = localStorage.getItem("ls:docs:langsmithUrl");
    const region =
      Object.keys(URLS).find((key) => URLS[key] === storedUrl) || "US";
    setSelectedRegion(region);
  }, []);

  const handleRegionChange = (region) => {
    setSelectedRegion(region);
    localStorage.setItem("ls:docs:langsmithUrl", URLS[region]);
    window.dispatchEvent(new Event("storage"));
  };

  return (
    <div className="navbar__item dropdown dropdown--hoverable">
      <div aria-haspopup="true" className="navbar__link">
        Region
      </div>
      <ul className="dropdown__menu" width="50px">
        <li
          onClick={() => handleRegionChange("US")}
          style={{
            width: "100%",
            color: selectedRegion === "US" ? "rgb(67, 147, 228)" : "white",
            cursor: "pointer",
            padding: "5px",
            textAlign: "center",
          }}
        >
          US
        </li>
        <li
          onClick={() => handleRegionChange("EU")}
          style={{
            width: "100%",
            color: selectedRegion === "EU" ? "rgb(67, 147, 228)" : "white",
            cursor: "pointer",
            padding: "5px",
            textAlign: "center",
          }}
        >
          EU
        </li>
      </ul>
    </div>
  );
}
