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
      <ul className="dropdown__menu regions-dropdown">
        <li
          onClick={() => handleRegionChange("US")}
          onKeyDown={() => {}}
          role="menuitem"
          style={{
            color:
              selectedRegion === "US" ? "var(--ifm-color-primary)" : "gray",
          }}
        >
          US
        </li>
        <li
          onClick={() => handleRegionChange("EU")}
          onKeyDown={() => {}}
          role="menuitem"
          style={{
            color:
              selectedRegion === "EU" ? "var(--ifm-color-primary)" : "gray",
          }}
        >
          EU
        </li>
      </ul>
    </div>
  );
}
