function renderSorting(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = ""; // Clear previous step

  stepData.state.forEach((value, index) => {
    const bar = document.createElement("div");
    bar.className = "bar";
    bar.style.height = value * 25 + "px"; // Scale bar height by value
    bar.innerText = value;

    // Apply highlight colors based on current action
    if (stepData.highlights.includes(index)) {
      if (stepData.action === "compare") bar.style.backgroundColor = "#f39c12"; // Yellow: comparing
      if (stepData.action === "swap") bar.style.backgroundColor = "#e74c3c"; // Red: swapping
      if (stepData.action === "done") bar.style.backgroundColor = "#2ecc71"; // Green: sorted
    }

    canvas.appendChild(bar);
  });

  // Update step description text
  document.getElementById("description").innerText = stepData.description;
}
