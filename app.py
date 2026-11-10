from flask import Flask, render_template, request, jsonify
from  algorithms.sorting import bubble_sort,insertion_sort,merge_sort,quick_sort
from algorithms.tree import bfs_tree,dfs_tree
from algorithms.searching import binary_search,linear_search
from algorithms.stack_queue_linked_list import stack_operations,queue_operations,linked_list_operations
from algorithms.dp_recursion import recursion_fib, dp_fib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sort", methods=["POST"])
def api_sort():
    data = request.get_json()
    arr = data.get("array", [5, 2, 8, 1, 9, 3])
    algo = data.get("algorithm", "bubble_sort")
    target = data.get("target", 8)
    if algo == "bubble_sort":
        steps = list(bubble_sort(arr))
    elif algo == "insertion_sort":
        steps = insertion_sort(arr)
    elif algo =="quick_sort":
        steps= quick_sort(arr)
    elif algo == "bfs_tree":
        steps = bfs_tree(arr)
    elif algo == "dfs_tree":
        steps = dfs_tree(arr)
    elif algo=="linear_search":
        steps = linear_search(arr,target)
    elif algo=="binary_search":
        steps=binary_search(arr,target)
    elif algo=="stack_operations":
        steps=stack_operations(arr)
    elif algo=="queue_operations":
        steps=queue_operations(arr)
    elif algo=="linked_list_operations":
        steps=linked_list_operations(arr)
    elif algo == "recursion_fib":
        steps = recursion_fib(arr)
    elif algo == "dp_fib":
        steps = dp_fib(arr)
    else:
        steps =merge_sort(arr)

    return jsonify({"steps": steps})

if __name__ == "__main__":
    app.run(debug=True)