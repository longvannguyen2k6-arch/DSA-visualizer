const player = {
  steps: [],
  currentIndex: 0,
  timer: null,
  speed: 500,
  renderFunc: renderSorting, // Default renderer

  loadSteps(steps, customRenderFunc = null) {
    this.pause();
    this.steps = steps;
    this.currentIndex = 0;
    if (customRenderFunc) this.renderFunc = customRenderFunc;
    if (this.steps.length > 0) {
      this.renderFunc(this.steps[0]);
    }
  },

  play() {
    if (this.timer) return; // Prevent multiple intervals
    this.timer = setInterval(() => {
      if (this.currentIndex < this.steps.length - 1) {
        this.currentIndex++;
        this.renderFunc(this.steps[this.currentIndex]);
      } else {
        this.pause(); // Stop when reaching the final step
      }
    }, this.speed);
  },

  pause() {
    clearInterval(this.timer);
    this.timer = null;
  },

  next() {
    this.pause();
    if (this.currentIndex < this.steps.length - 1) {
      this.currentIndex++;
      this.renderFunc(this.steps[this.currentIndex]);
    }
  },

  prev() {
    this.pause();
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.renderFunc(this.steps[this.currentIndex]);
    }
  },

  setSpeed(newSpeed) {
    this.speed = parseInt(newSpeed);
    if (this.timer) {
      this.pause();
      this.play(); // Restart interval with updated speed
    }
  },
};

// Fetch sorting steps from Flask backend
async function loadSorting() {
  const rawInput = document.getElementById("array-input").value;
  const algo = document.getElementById("algo-select").value;
  const targetInput = document.getElementById("target-input");
  const target = targetInput ? parseInt(targetInput.value) || 0 : 0;
  const arr = rawInput
    .split(",")
    .map((num) => parseInt(num.trim()))
    .filter((n) => !isNaN(n));

  const response = await fetch("/api/sort", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ array: arr, algorithm: algo, target: target }),
  });
  const data = await response.json();
  let chosenRenderer = renderSorting;
  if (algo.includes("tree")) chosenRenderer = renderTree;
  else if (algo.includes("search")) chosenRenderer = renderSearching;

  player.loadSteps(data.steps, chosenRenderer);
}

// Auto-load initial visualization on page load
window.onload = loadSorting;
