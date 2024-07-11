import React from "react";

const URLS = {
  US: "https://smith.langchain.com",
  EU: "https://eu.smith.langchain.com",
};

export default function RegionSelector(props) {
  const handleRegionChange = (region) => {
    localStorage.setItem("ls:docs:langsmithUrl", URLS[region]);
    window.dispatchEvent(new Event("storage"));
  };
  return (
    <div className="navbar__item dropdown dropdown--hoverable dropdown--right">
      <a href="#" aria-haspopup="true" role="button" className="navbar__link">
        Region
      </a>
      <ul className="dropdown__menu">
        <li onClick={() => handleRegionChange("US")}>US</li>
        <li onClick={() => handleRegionChange("EU")}>EU</li>
      </ul>
    </div>
  );
}
