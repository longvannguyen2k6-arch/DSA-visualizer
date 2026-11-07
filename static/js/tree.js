function renderTree(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";
  // Change canvas layout from column bars to vertical tree levels
  canvas.style.display = "flex";
  canvas.style.flexDirection = "column";
  canvas.style.alignItems = "center";
  canvas.style.justifyContent = "flex-start";
  canvas.style.gap = "25px";

  const arr = stepData.state;
  const visited = stepData.visited || [];
  let level = 0;
  let index = 0;

  // Group array elements into binary tree levels (1, 2, 4, 8...)
  while (index < arr.length) {
    const levelDiv = document.createElement("div");
    levelDiv.style.display = "flex";
    levelDiv.style.justifyContent = "center";
    levelDiv.style.gap = 160 / (level + 1) + "px";

    const nodesInLevel = Math.pow(2, level);
    for (let i = 0; i < nodesInLevel && index < arr.length; i++) {
      const node = document.createElement("div");
      node.innerText = arr[index];
      node.style.width = "45px";
      node.style.height = "45px";
      node.style.borderRadius = "50%"; // Circle node
      node.style.display = "flex";
      node.style.alignItems = "center";
      node.style.justifyContent = "center";
      node.style.color = "white";
      node.style.fontWeight = "bold";
      node.style.backgroundColor = "#3498db"; // Default blue

      // Already visited nodes -> Green
      if (visited.includes(index) || stepData.action === "done") {
        node.style.backgroundColor = "#2ecc71";
      }
      // Currently visiting node -> Yellow/Orange
      if (stepData.highlights.includes(index) && stepData.action !== "done") {
        node.style.backgroundColor = "#f39c12";
        node.style.transform = "scale(1.2)";
      }

      levelDiv.appendChild(node);
      index++;
    }
    canvas.appendChild(levelDiv);
    level++;
  }

  document.getElementById("description").innerText = stepData.description;
}
