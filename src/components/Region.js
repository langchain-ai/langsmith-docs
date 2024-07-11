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
      <ul className="dropdown__menu" style={{ width: "100%" }}>
        <li>
          <a
            onClick={() => handleRegionChange("US")}
            style={{
              className:
                selectedRegion === "US"
                  ? "dropdown__link--active dropdown__link"
                  : "dropdown__link",
            }}
          >
            US
          </a>
        </li>
        <li>
          <a
            onClick={() => handleRegionChange("EU")}
            style={{
              className:
                selectedRegion === "EU"
                  ? "dropdown__link dropdown__link--active"
                  : "dropdown__link",
            }}
          >
            EU
          </a>
        </li>
      </ul>
    </div>
  );
}
