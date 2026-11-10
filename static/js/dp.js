function renderDP(stepData) {
    const canvas = document.getElementById("canvas");
    canvas.innerHTML = "";
    canvas.style.flexDirection = "row";
    canvas.style.alignItems = "center";
    canvas.style.justifyContent = "center";

    stepData.state.forEach((value, index) => {
        const cell = document.createElement("div");
        cell.style.width = "60px";
        cell.style.height = "65px";
        cell.style.backgroundColor = value === "?" ? "#bdc3c7" : "#3498db";
        cell.style.color = "white";
        cell.style.fontWeight = "bold";
        cell.style.display = "flex";
        cell.style.flexDirection = "column";
        cell.style.alignItems = "center";
        cell.style.justifyContent = "center";
        cell.style.borderRadius = "6px";
        cell.innerHTML = `<small style="font-size:10px; opacity:0.85;">dp[${index}]</small><span style="font-size:18px;">${value}</span>`;

        if (stepData.highlights.includes(index)) {
            if (stepData.action === "compare") cell.style.backgroundColor = "#f39c12"; // Yellow: reading previous states
            if (stepData.action === "swap") cell.style.backgroundColor = "#e74c3c";    // Red: writing new state
            if (stepData.action === "done") {
                cell.style.backgroundColor = "#2ecc71"; // Green: final answer
                cell.style.transform = "scale(1.15)";
            }
        }
        canvas.appendChild(cell);
    });

    document.getElementById("description").innerText = stepData.description;
}