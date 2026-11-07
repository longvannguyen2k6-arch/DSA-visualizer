from collections import deque
def bfs_tree(arr):
    steps = []
    n = len(arr)
    a = arr.copy()
    visited = []
    queue = deque([0]) if n > 0 else deque()
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "visited": [],
        "action": "init",
        "description": "Initial Binary Tree (Array representation)"
    })
    while queue:
        curr = queue.popleft()
        steps.append({
            "state": a.copy(),
            "visited": visited.copy(),
            "highlights": [curr],
            "action": "compare",
            "description": f"BFS visiting node {a[curr]} (index {curr})"
        })
        visited.append(curr)
        left = 2 * curr + 1
        right = 2 * curr + 2
        if left < n:
            queue.append(left)
        if right < n:
            queue.append(right)
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "visited": visited.copy(),
        "action": "done",
        "description": f"BFS Traversal completed! Order: {[a[i] for i in visited]}"
    })
    return steps

def dfs_tree(arr):
    steps = []
    n = len(arr)
    a = arr.copy()
    visited = []  # Track already visited node indices

    # Initial state
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "visited": [],
        "action": "init",
        "description": "Initial Binary Tree (Array representation)"
    })

    def _dfs(curr):
        # Base case: stop if index is out of bounds
        if curr >= n:
            return

        # 1. Record step when visiting the current node
        steps.append({
            "state": a.copy(),
            "highlights": [curr],
            "visited": visited.copy(),
            "action": "compare",
            "description": f"DFS visiting node {a[curr]} (index {curr})"
        })

        # Mark current node as visited
        visited.append(curr)

        # 2. Recursively traverse Left child (2 * curr + 1)
        _dfs(2 * curr + 1)

        # 3. Recursively traverse Right child (2 * curr + 2)
        _dfs(2 * curr + 2)

    # Start DFS from the root node (index 0)
    if n > 0:
        _dfs(0)

    # Final completed state
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "visited": visited.copy(),
        "action": "done",
        "description": f"DFS Traversal completed! Order: {[a[i] for i in visited]}"
    })
    return steps
