function renderStack(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";
  canvas.style.flexDirection = "column-reverse"; // Stack grows upwards
  canvas.style.alignItems = "center";
  canvas.style.justifyContent = "flex-start";
  canvas.style.gap = "8px";

  stepData.state.forEach((value, index) => {
    const box = document.createElement("div");
    box.style.width = "120px";
    box.style.height = "38px";
    box.style.backgroundColor = "#3498db";
    box.style.color = "white";
    box.style.fontWeight = "bold";
    box.style.display = "flex";
    box.style.alignItems = "center";
    box.style.justifyContent = "center";
    box.style.borderRadius = "4px";
    box.innerText =
      index === stepData.state.length - 1 ? `${value} (TOP)` : value;

    if (stepData.highlights.includes(index)) {
      if (stepData.action === "push") box.style.backgroundColor = "#e74c3c";
      if (stepData.action === "compare") box.style.backgroundColor = "#f39c12";
      if (stepData.action === "pop") box.style.backgroundColor = "#9b59b6";
      if (stepData.action === "done") box.style.backgroundColor = "#2ecc71";
    }
    canvas.appendChild(box);
  });

  document.getElementById("description").innerText = stepData.description;
}

function renderQueue(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";
  canvas.style.flexDirection = "row";
  canvas.style.alignItems = "center";
  canvas.style.justifyContent = "center";
  canvas.style.gap = "8px";

  stepData.state.forEach((value, index) => {
    const box = document.createElement("div");
    box.style.width = "75px";
    box.style.height = "55px";
    box.style.backgroundColor = "#3498db";
    box.style.color = "white";
    box.style.fontWeight = "bold";
    box.style.display = "flex";
    box.style.flexDirection = "column";
    box.style.alignItems = "center";
    box.style.justifyContent = "center";
    box.style.borderRadius = "6px";

    let label = "";
    if (index === 0 && index === stepData.state.length - 1) {
      label = "FRONT / REAR";
    } else if (index === 0) {
      label = "FRONT";
    } else if (index === stepData.state.length - 1) {
      label = "REAR";
    }

    box.innerHTML = `<span>${value}</span><small style="font-size:10px; opacity:0.85;">${label}</small>`;

    if (stepData.highlights.includes(index)) {
      if (stepData.action === "enqueue") box.style.backgroundColor = "#2ecc71";
      if (stepData.action === "compare") box.style.backgroundColor = "#f39c12";
      if (stepData.action === "dequeue") box.style.backgroundColor = "#e74c3c";
      if (stepData.action === "done") box.style.backgroundColor = "#2ecc71";
    }

    canvas.appendChild(box);
  });

  document.getElementById("description").innerText = stepData.description;
}

function renderLinkedList(stepData) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";
  canvas.style.flexDirection = "row";
  canvas.style.alignItems = "center";
  canvas.style.justifyContent = "center";
  canvas.style.gap = "8px";

  stepData.state.forEach((value, index) => {
    const wrapper = document.createElement("div");
    wrapper.style.display = "flex";
    wrapper.style.alignItems = "center";
    wrapper.style.gap = "8px";

    const node = document.createElement("div");
    node.style.padding = "12px 16px";
    node.style.backgroundColor = "#3498db";
    node.style.color = "white";
    node.style.fontWeight = "bold";
    node.style.borderRadius = "6px";
    node.innerText = index === 0 ? `HEAD: ${value}` : `[${value}]`;

    if (stepData.highlights.includes(index)) {
      if (stepData.action === "insert") node.style.backgroundColor = "#e74c3c";
      if (stepData.action === "compare") node.style.backgroundColor = "#f39c12";
      if (stepData.action === "delete") node.style.backgroundColor = "#9b59b6";
      if (stepData.action === "done") node.style.backgroundColor = "#2ecc71";
    }

    const arrow = document.createElement("span");
    arrow.style.fontWeight = "bold";
    arrow.style.fontSize = "20px";
    arrow.innerText = "→";

    wrapper.appendChild(node);
    wrapper.appendChild(arrow);
    canvas.appendChild(wrapper);
  });

  const nullNode = document.createElement("div");
  nullNode.style.fontWeight = "bold";
  nullNode.style.color = "#7f8c8d";
  nullNode.innerText = "NULL";
  canvas.appendChild(nullNode);

  document.getElementById("description").innerText = stepData.description;
}
