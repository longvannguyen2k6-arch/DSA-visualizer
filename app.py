from flask import Flask, render_template, request, jsonify
from analysis import get_complexity
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from algorithms.searching import linear_search, binary_search, sliding_window, two_pointers
from algorithms.tree import bfs_tree, dfs_tree
from algorithms.stack_queue_linked_list import (
    stack_operations,
    queue_operations,
    linked_list_operations,
)
from algorithms.dp_recursion import recursion_fib, dp_fib

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sorting", methods=["POST"])
def api_sorting():
    data = request.get_json() or {}
    arr = data.get("array") or [5, 2, 8, 1, 9, 3]
    algo = data.get("algorithm", "bubble_sort")

    if algo == "bubble_sort":
        steps = list(bubble_sort(arr))
    elif algo == "insertion_sort":
        steps = insertion_sort(arr)
    elif algo == "quick_sort":
        steps = quick_sort(arr)
    else:
        steps = merge_sort(arr)

    return jsonify({
    "steps": steps,
    "complexity": get_complexity(algo)
})
@app.route("/api/searching", methods=["POST"])
def api_searching():
    data = request.get_json() or {}
    arr = data.get("array") or [5, 2, 8, 1, 9, 3]
    algo = data.get("algorithm", "linear_search")
    target = data.get("target")
    if target is None:
        target = 8
    else:
        try:
            target = int(target)
        except (ValueError, TypeError):
            target = 8

    if algo == "linear_search":
        steps = linear_search(arr, target)
    elif algo == "binary_search":
        steps = binary_search(arr, target)
    elif algo == "sliding_window":
        steps = sliding_window(arr, target)
    else:
        steps = two_pointers(arr, target)

    return jsonify({
    "steps": steps,
    "complexity": get_complexity(algo)
})


@app.route("/api/tree", methods=["POST"])
def api_tree():
    data = request.get_json() or {}
    arr = data.get("array") or [5, 2, 8, 1, 9, 3]
    algo = data.get("algorithm", "bfs_tree")

    if algo == "bfs_tree":
        steps = bfs_tree(arr)
    else:
        steps = dfs_tree(arr)

    return jsonify({
    "steps": steps,
    "complexity": get_complexity(algo)
})
@app.route("/api/structures", methods=["POST"])
def api_structures():
    data = request.get_json() or {}
    arr = data.get("array") or [5, 2, 8, 1, 9, 3]
    algo = data.get("algorithm", "stack_operations")

    if algo in ("stack", "stack_operations"):
        steps = stack_operations(arr)
    elif algo in ("queue", "queue_operations"):
        steps = queue_operations(arr)
    else:
        steps = linked_list_operations(arr)

    return jsonify({
    "steps": steps,
    "complexity": get_complexity(algo)
})

@app.route("/api/dp_recursion", methods=["POST"])
def api_dp_recursion():
    data = request.get_json() or {}
    arr = data.get("array") or [5, 2, 8, 1, 9, 3]
    algo = data.get("algorithm", "recursion_fib")

    if algo == "recursion_fib":
        steps = recursion_fib(arr)
    else:
        steps = dp_fib(arr)

    return jsonify({
    "steps": steps,
    "complexity": get_complexity(algo)
})


if __name__ == "__main__":
    app.run(debug=True)