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
    if (this.currentIndex >= this.steps.length - 1) {
      this.currentIndex = 0;
      if (this.steps.length > 0) {
        this.renderFunc(this.steps[0]);
      }
    }
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

  let endpoint = "/api/sorting";
  let chosenRenderer = renderSorting;

  if (algo.includes("tree")) {
    endpoint = "/api/tree";
    chosenRenderer = renderTree;
  } else if (
    algo.includes("search") ||
    algo === "sliding_window" ||
    algo === "two_pointers"
  ) {
    endpoint = "/api/searching";
    chosenRenderer = renderSearching;
  } else if (algo.includes("stack")) {
    endpoint = "/api/structures";
    chosenRenderer = renderStack;
  } else if (algo.includes("queue")) {
    endpoint = "/api/structures";
    chosenRenderer = renderQueue;
  } else if (algo.includes("linked_list")) {
    endpoint = "/api/structures";
    chosenRenderer = renderLinkedList;
  } else if (algo === "recursion_fib") {
    endpoint = "/api/dp_recursion";
    chosenRenderer = renderStack;
  } else if (algo === "dp_fib") {
    endpoint = "/api/dp_recursion";
    chosenRenderer = renderDP;
  }
  const response = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ array: arr, algorithm: algo, target: target }),
  });

  const data = await response.json();
  player.loadSteps(data.steps, chosenRenderer);
  updateComplexityUI(data.complexity);
}
function updateComplexityUI(comp) {
  if (!comp) return;
  document.getElementById("comp-name").innerText =
    `${comp.name} — Complexity Analysis`;
  document.getElementById("comp-best").innerText = comp.best;
  document.getElementById("comp-avg").innerText = comp.average;
  document.getElementById("comp-worst").innerText = comp.worst;
  document.getElementById("comp-space").innerText = comp.space;
  document.getElementById("comp-note").innerText = comp.note;
}
const ALGO_CATEGORIES = {
  sorting: [
    { value: "bubble_sort", text: "Bubble Sort" },
    { value: "insertion_sort", text: "Insertion Sort" },
    { value: "merge_sort", text: "Merge Sort" },
    { value: "quick_sort", text: "Quick Sort" },
  ],
  searching: [
    { value: "linear_search", text: "Linear Search" },
    { value: "binary_search", text: "Binary Search" },
    { value: "sliding_window", text: "Sliding Window (Max Sum K)" },
    { value: "two_pointers", text: "Two Pointers (Pair Sum)" },
  ],
  tree: [
    { value: "bfs_tree", text: "Tree BFS" },
    { value: "dfs_tree", text: "Tree DFS" },
  ],
  structures: [
    { value: "stack_operations", text: "Stack (LIFO)" },
    { value: "queue_operations", text: "Queue (FIFO)" },
    { value: "linked_list_operations", text: "Linked List" },
  ],
  dp_recursion: [
    { value: "recursion_fib", text: "Recursion (Fibonacci Call Stack)" },
    { value: "dp_fib", text: "Dynamic Programming (Fibonacci Table)" },
  ],
};

function updateAlgoOptions() {
  const category = document.getElementById("category-select").value;
  const algoSelect = document.getElementById("algo-select");
  algoSelect.innerHTML = "";
  ALGO_CATEGORIES[category].forEach((item) => {
    const opt = document.createElement("option");
    opt.value = item.value;
    opt.innerText = item.text;
    algoSelect.appendChild(opt);
  });

  const targetInput = document.getElementById("target-input");
  if (targetInput) {
    targetInput.style.display =
      category === "searching" ? "inline-block" : "none";
  }
  loadSorting();
}
window.onload = updateAlgoOptions;
