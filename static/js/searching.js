function renderSearching(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";
  canvas.style.flexDirection = "row";
  canvas.style.alignItems = "center";
  canvas.style.justifyContent = "center";
  canvas.style.gap = "8px";

  stepData.state.forEach((value, index) => {
    const box = document.createElement("div");
    box.style.width = "55px";
    box.style.height = "55px";
    box.style.backgroundColor = "#3498db"; // Default blue
    box.style.color = "white";
    box.style.fontWeight = "bold";
    box.style.display = "flex";
    box.style.flexDirection = "column";
    box.style.alignItems = "center";
    box.style.justifyContent = "center";
    box.style.borderRadius = "6px";
    box.innerHTML = `<span>${value}</span><small style="font-size:10px; opacity:0.8;">idx:${index}</small>`;

    if (stepData.highlights.includes(index)) {
      if (stepData.action === "compare") box.style.backgroundColor = "#f39c12"; // Yellow: checking
      if (stepData.action === "done") {
        box.style.backgroundColor = "#2ecc71"; // Green: found!
        box.style.transform = "scale(1.15)";
      }
    }

    if (stepData.action === "not_found") {
      box.style.backgroundColor = "#95a5a6"; // Gray out all boxes if not found
    }

    canvas.appendChild(box);
  });

  document.getElementById("description").innerText = stepData.description;
}
