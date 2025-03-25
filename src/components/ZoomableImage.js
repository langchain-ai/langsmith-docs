import React, { useState, useRef, useEffect } from "react";

export const ZoomableImage = ({ src, alt, width }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [scale, setScale] = useState(1);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const containerRef = useRef(null);
  const imageSrc = require(`@site/docs${src}`).default;

  // Prevent background scroll when modal is open
  useEffect(() => {
    if (isModalOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [isModalOpen]);

  // Reset zoom and position when modal closes
  useEffect(() => {
    if (!isModalOpen) {
      setScale(1);
      setPosition({ x: 0, y: 0 });
    }
  }, [isModalOpen]);

  const handleWheel = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const delta = e.deltaY * -0.01;
    // Only allow zooming in: scale never goes below 1
    const newScale = Math.min(Math.max(1, scale + delta), 4);
    setScale(newScale);
  };

  const handleMouseDown = (e) => {
    // Only allow dragging when zoomed in
    if (scale === 1) return;
    e.preventDefault();
    setIsDragging(true);
    setDragStart({
      x: e.clientX - position.x,
      y: e.clientY - position.y,
    });
  };

  const handleMouseMove = (e) => {
    if (isDragging) {
      setPosition({
        x: e.clientX - dragStart.x,
        y: e.clientY - dragStart.y,
      });
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  // When scale is 1, ignore any translation so the image is centered by the flex container.
  const transformStyle =
    scale === 1
      ? `scale(1)`
      : `scale(${scale}) translate(${position.x / scale}px, ${
          position.y / scale
        }px)`;

  return (
    <>
      <div
        style={{ cursor: "pointer", display: "inline-block" }}
        onClick={() => setIsModalOpen(true)}
      >
        <img
          src={imageSrc}
          alt={alt}
          style={{
            maxWidth: width || "100%",
            transition: "transform 0.2s",
          }}
          className="zoomable-img"
        />
      </div>

      {isModalOpen && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: "rgba(0, 0, 0, 0.8)",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 1000,
          }}
          onClick={() => setIsModalOpen(false)}
          onWheel={handleWheel}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseUp}
        >
          <div
            ref={containerRef}
            style={{
              position: "relative",
              maxWidth: "90vw",
              maxHeight: "90vh",
              cursor: isDragging ? "grabbing" : scale > 1 ? "grab" : "default",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <img
              src={imageSrc}
              alt={alt}
              style={{
                maxWidth: "100%",
                maxHeight: "90vh",
                objectFit: "contain",
                transform: transformStyle,
                transition: isDragging ? "none" : "transform 0.1s",
              }}
              onMouseDown={handleMouseDown}
              draggable={false}
            />
            <button
              onClick={() => setIsModalOpen(false)}
              style={{
                position: "absolute",
                top: "-40px",
                right: "-40px",
                background: "none",
                border: "none",
                color: "white",
                fontSize: "24px",
                cursor: "pointer",
                padding: "10px",
              }}
            >
              ✕
            </button>
          </div>
        </div>
      )}
    </>
  );
};
