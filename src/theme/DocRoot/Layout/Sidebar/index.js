import React from "react";
import Sidebar from "@theme-original/DocRoot/Layout/Sidebar";
import { useState, useEffect } from "react";
import { useLocation } from "@docusaurus/router";

export default function SidebarWrapper(props) {
  const [isVisible, setIsVisible] = useState(true);
  const location = useLocation();

  // Reset sidebar visibility when navigating to a new page
  useEffect(() => {
    setIsVisible(true);
  }, [location]);

  return (
    <div
      className={`custom-sidebar-wrapper ${
        !isVisible ? "sidebar-collapsed" : ""
      }`}
    >
      <div className="custom-sidebar-container">
        <button
          className="custom-sidebar-toggle"
          onClick={() => setIsVisible(!isVisible)}
          aria-label={isVisible ? "Collapse sidebar" : "Expand sidebar"}
          title={isVisible ? "Collapse sidebar" : "Expand sidebar"}
        >
          {isVisible ? "←|" : "|→"}
        </button>
        <div className="custom-sidebar-content">
          <Sidebar {...props} />
        </div>
      </div>
    </div>
  );
}
