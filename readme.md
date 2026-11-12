# 🚀 DSA Visualizer — Interactive Data Structures & Algorithms

An interactive, responsive web application for visualizing classic data structures and computer science algorithms in real time. Built with a **Python (Flask)** backend and a pure **HTML5 / CSS3 / Vanilla JavaScript** frontend.

---

## 🌟 Key Features

### 1. Comprehensive Algorithm Catalog (15 Algorithms & Data Structures)
* **Sorting Algorithms:** Bubble Sort, Insertion Sort, Merge Sort, Quick Sort.
* **Searching & Pointer Techniques:** Linear Search, Binary Search, Sliding Window (Max Sum of Subarray $K$), Two Pointers (Pair Sum).
* **Tree Traversals:** Tree BFS (Breadth-First Search, Level Order), Tree DFS (Depth-First Search, Pre-order).
* **Data Structures:**
  * **Stack (LIFO):** Push, Pop, Peek operations with top indicator.
  * **Queue (FIFO):** Enqueue, Dequeue, Front inspection with `FRONT` and `REAR` pointers.
  * **Singly Linked List:** Node insertion at tail, sequential traversal, and head deletion (`HEAD -> [node] -> NULL`).
* **Recursion & Dynamic Programming:**
  * **Fibonacci Call Stack:** Visualizing recursive branching and the execution call stack.
  * **Fibonacci DP Table:** Visualizing bottom-up tabulation with memoized state lookups.

### 2. Full-Featured Interactive Player
* **Playback Controls:** ▶ **Play**, ⏸ **Pause**, ⏭ **Next Step**, ⏮ **Previous Step**.
* **Seamless Replay:** Automatically restarts from step 0 when clicking Play at the end of an animation.
* **Dynamic Speed Slider:** Real-time delay adjustment from **100 ms to 1500 ms** with a live millisecond counter.
* **Custom Input:** Easily test custom comma-separated arrays and target values.

### 3. Vivid 3D Visual Feedback & Neon Glow Effects
* **Non-destructive Rendering:** JavaScript state colors are enhanced with glossy 3D highlights and contextual neon glows:
  * 🟡 **Amber / Yellow (`#f39c12`):** Comparing elements / active pointer inspection.
  * 🔴 **Crimson / Red (`#e74c3c`):** Swapping elements or pushing into structures.
  * 🟣 **Purple (`#9b59b6`):** Popping / deleting nodes.
  * 🟢 **Emerald / Green (`#2ecc71`):** Target found or sorting completed (with celebratory bounce animation).
* **Subtle Blueprint Grid:** Clean laboratory grid canvas for accurate height and position tracking.

### 4. Big-O Complexity Dashboard
* Displays **Best Time**, **Average Time**, **Worst Time**, and **Space Complexity** badges alongside a concise conceptual explanation for every selected algorithm.

### 5. Automated Test Suite
* Pre-configured with **17 automated unit and integration tests** covering all algorithm generators and Flask API endpoints.

---

## 📁 Project Structure

```text
DSA-visualizer/
│
├── algorithms/                    # Algorithm implementations & step generators
│   ├── dp_recursion.py            # Fibonacci Call Stack & DP Tabulation
│   ├── searching.py               # Linear, Binary, Sliding Window, Two Pointers
│   ├── sorting.py                 # Bubble, Insertion, Merge, Quick Sort
│   ├── stack_queue_linked_list.py # Stack, Queue, and Linked List operations
│   └── tree.py                    # Binary Tree BFS & DFS Traversals
│
├── static/                        # Frontend assets
│   ├── css/
│   │   └── style.css              # Custom styling, 3D highlights & animations
│   └── js/
│       ├── dp.js                  # Dynamic Programming table renderer
│       ├── player.js              # Media player controller & API dispatcher
│       ├── searching.js           # Search box & index renderer
│       ├── sorting.js             # Sorting bar chart renderer
│       ├── stack_queue_linked_list.js # Stack, Queue & Linked List renderers
│       └── tree.js                # Binary tree hierarchical level renderer
│
├── templates/
│   └── index.html                 # Main single-page application template
│
├── analysis.py                    # Big-O complexity lookup table
├── app.py                         # Flask web server & RESTful API routes
├── test.py                        # Automated Pytest test suite (17 tests)
└── readme.md                      # Project documentation
```

---

## 🛠️ Installation & Setup

### Prerequisites
* **Python 3.9+** installed on your system.

### 1. Install Dependencies
Open your terminal in the project directory and install the required packages:

```bash
pip install flask pytest
```

### 2. Run the Application
Start the Flask development server:

```bash
python app.py
```

### 3. Open in Browser
Visit the following URL in your web browser:
```text
http://127.0.0.1:5000/
```

---

## 🧪 Running the Test Suite

The project includes 17 automated tests verifying algorithm correctness, edge-case resilience, and API responses. Run the tests using any of the following commands:

```bash
# Option 1: Run directly with Python (built-in runner)
python test.py

# Option 2: Run via pytest
pytest test.py

# Option 3: Run with verbose per-test output
pytest -v test.py
```

### Expected Output:
```text
============================= test session starts =============================
collected 17 items

test.py::test_sorting_algorithms[bubble_sort] PASSED                     [  5%]
test.py::test_sorting_algorithms[insertion_sort] PASSED                  [ 11%]
test.py::test_sorting_algorithms[merge_sort] PASSED                      [ 17%]
test.py::test_sorting_algorithms[quick_sort] PASSED                      [ 23%]
test.py::test_linear_and_binary_search PASSED                            [ 29%]
test.py::test_sliding_window_and_two_pointers PASSED                     [ 35%]
test.py::test_tree_traversals PASSED                                     [ 41%]
test.py::test_data_structures[stack_operations] PASSED                   [ 47%]
test.py::test_data_structures[queue_operations] PASSED                   [ 52%]
test.py::test_data_structures[linked_list_operations] PASSED             [ 58%]
test.py::test_dp_and_recursion PASSED                                    [ 64%]
test.py::test_complexity_analysis PASSED                                 [ 70%]
test.py::test_flask_api_routes[/api/sorting-merge_sort] PASSED           [ 76%]
test.py::test_flask_api_routes[/api/searching-sliding_window] PASSED     [ 82%]
test.py::test_flask_api_routes[/api/tree-bfs_tree] PASSED                [ 88%]
test.py::test_flask_api_routes[/api/structures-stack_operations] PASSED  [ 94%]
test.py::test_flask_api_routes[/api/dp_recursion-dp_fib] PASSED          [100%]

============================= 17 passed in 0.09s ==============================
```

---

## 🎮 How to Use

1. **Select Category:** Use the first dropdown to choose a domain (*Sorting, Searching, Tree, Data Structures, or DP & Recursion*).
2. **Select Algorithm:** The second dropdown automatically updates with algorithms relevant to the chosen category.
3. **Configure Inputs:**
   * **Array Input:** Enter custom comma-separated numbers (e.g., `5, 2, 8, 1, 9, 4, 11, 10`).
   * **Target Input:** When selecting Searching algorithms or Two Pointers / Sliding Window, enter the target value or window size $K$.
4. **Load Data:** Click **"Load Data"** to fetch step data and render the initial state.
5. **Playback Control:**
   * Click **▶ Play** to watch the automated visualization.
   * Click **⏸ Pause** to inspect the current state.
   * Use **⏮ Prev / ⏭ Next** to step through the algorithm manually.
   * Drag the **Delay slider** to speed up or slow down execution in real time.
