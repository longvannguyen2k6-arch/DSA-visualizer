import pytest
from app import app
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


@pytest.mark.parametrize("sort_func", [bubble_sort, insertion_sort, merge_sort, quick_sort])
def test_sorting_algorithms(sort_func):
    arr = [5, 2, 8, 1, 9, 3]
    steps = list(sort_func(arr))
    assert len(steps) > 0
    assert steps[-1]["state"] == [1, 2, 3, 5, 8, 9]
    assert steps[-1]["action"] == "done"



def test_linear_and_binary_search():
    arr = [5, 2, 8, 1, 9, 3]
    
    lin_steps = linear_search(arr, 8)
    bin_steps = binary_search(arr, 8)
    assert lin_steps[-1]["action"] == "done"
    assert bin_steps[-1]["action"] == "done"


    not_found_steps = binary_search(arr, 99)
    assert not_found_steps[-1]["action"] == "not_found"


def test_sliding_window_and_two_pointers():
    arr = [5, 2, 8, 1, 9, 3]
    sw_steps = sliding_window(arr, 3)
    assert sw_steps[-1]["action"] == "done"
    assert len(sw_steps[-1]["highlights"]) == 3  

    
    tp_found = two_pointers(arr, 11)
    assert tp_found[-1]["action"] == "done"


    tp_not_found = two_pointers(arr, 99)
    assert tp_not_found[-1]["action"] == "not_found"


def test_tree_traversals():
    arr = [5, 2, 8, 1, 9]
    bfs_steps = bfs_tree(arr)
    dfs_steps = dfs_tree(arr)
    assert bfs_steps[-1]["action"] == "done"
    assert dfs_steps[-1]["action"] == "done"


@pytest.mark.parametrize("ds_func", [stack_operations, queue_operations, linked_list_operations])
def test_data_structures(ds_func):
    arr = [10, 20, 30]
    steps = ds_func(arr)
    assert len(steps) > 0
    assert steps[-1]["action"] == "done"


def test_dp_and_recursion():
    rec_steps = recursion_fib([5])
    dp_steps = dp_fib([5])
    assert rec_steps[-1]["action"] == "done"
    assert "5" in rec_steps[-1]["state"][0]  # Fibonacci(5) = 5
    assert dp_steps[-1]["action"] == "done"
    assert dp_steps[-1]["state"][-1] == 5    # Ô cuối bảng DP dp[5] == 5


def test_complexity_analysis():
    comp = get_complexity("quick_sort")
    assert comp["best"] == "O(n log n)"
    assert comp["worst"] == "O(n²)"


@pytest.mark.parametrize("endpoint,algo", [
    ("/api/sorting", "merge_sort"),
    ("/api/searching", "sliding_window"),
    ("/api/tree", "bfs_tree"),
    ("/api/structures", "stack_operations"),
    ("/api/dp_recursion", "dp_fib"),
])
def test_flask_api_routes(endpoint, algo):
    client = app.test_client()
    response = client.post(endpoint, json={
        "array": [5, 2, 8, 1, 9, 3],
        "algorithm": algo,
        "target": 3
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "steps" in data and len(data["steps"]) > 0
    assert "complexity" in data and data["complexity"]["name"] != "Unknown Algorithm"


if __name__ == "__main__":
    pytest.main(["-v", "test.py"])