COMPLEXITY_DATA = {
    "bubble_sort": {
        "name": "Bubble Sort",
        "best": "O(n)", "average": "O(n²)", "worst": "O(n²)", "space": "O(1)",
        "note": "Repeatedly swaps adjacent elements if they are in the wrong order."
    },
    "insertion_sort": {
        "name": "Insertion Sort",
        "best": "O(n)", "average": "O(n²)", "worst": "O(n²)", "space": "O(1)",
        "note": "Builds the sorted array one item at a time by shifting larger elements."
    },
    "merge_sort": {
        "name": "Merge Sort",
        "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n log n)", "space": "O(n)",
        "note": "Divide-and-conquer algorithm that splits the array in half and merges sorted halves."
    },
    "quick_sort": {
        "name": "Quick Sort",
        "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n²)", "space": "O(log n)",
        "note": "Partitions the array around a pivot element so smaller items are on the left."
    },
    "linear_search": {
        "name": "Linear Search",
        "best": "O(1)", "average": "O(n)", "worst": "O(n)", "space": "O(1)",
        "note": "Sequentially checks each element of the list until a match is found."
    },
    "binary_search": {
        "name": "Binary Search",
        "best": "O(1)", "average": "O(log n)", "worst": "O(log n)", "space": "O(1)",
        "note": "Halves the search space at each step on a sorted array."
    },
    "sliding_window": {
        "name": "Sliding Window (Fixed Size K)",
        "best": "O(n)", "average": "O(n)", "worst": "O(n)", "space": "O(1)",
        "note": "Reuses the sum of the previous window to avoid redundant O(n*k) recalculations."
    },
    "two_pointers": {
        "name": "Two Pointers (Sorted Array)",
        "best": "O(1)", "average": "O(n)", "worst": "O(n)", "space": "O(1)",
        "note": "Moves left and right pointers inward on a sorted array to find a target pair."
    },
    "bfs_tree": {
        "name": "Breadth-First Search (Tree)",
        "best": "O(V)", "average": "O(V + E)", "worst": "O(V + E)", "space": "O(W)",
        "note": "Explores nodes level by level using a FIFO Queue (W = max width of tree)."
    },
    "dfs_tree": {
        "name": "Depth-First Search (Tree)",
        "best": "O(V)", "average": "O(V + E)", "worst": "O(V + E)", "space": "O(H)",
        "note": "Explores as deep as possible along each branch using recursion (H = tree height)."
    },
    "stack_operations": {
        "name": "Stack (LIFO)",
        "best": "O(1)", "average": "O(1)", "worst": "O(1)", "space": "O(n)",
        "note": "Push, Pop, and Peek operations at the top of the stack all run in O(1) constant time."
    },
    "queue_operations": {
        "name": "Queue (FIFO)",
        "best": "O(1)", "average": "O(1)", "worst": "O(1)", "space": "O(n)",
        "note": "Enqueue at rear and Dequeue from front operate in FIFO order."
    },
    "linked_list_operations": {
        "name": "Singly Linked List",
        "best": "O(1)", "average": "O(n)", "worst": "O(n)", "space": "O(n)",
        "note": "Head insertion/deletion is O(1), while searching or traversing takes O(n)."
    },
    "recursion_fib": {
        "name": "Pure Recursion (Fibonacci)",
        "best": "O(1)", "average": "O(2ⁿ)", "worst": "O(2ⁿ)", "space": "O(n)",
        "note": "Exponential time due to recomputing overlapping subproblems on the Call Stack."
    },
    "dp_fib": {
        "name": "Dynamic Programming (Tabulation)",
        "best": "O(n)", "average": "O(n)", "worst": "O(n)", "space": "O(n)",
        "note": "Stores intermediate results in a bottom-up table to achieve linear O(n) time."
    }
}


def get_complexity(algo_key):
    aliases = {
        "stack": "stack_operations",
        "queue": "queue_operations",
        "linked_list": "linked_list_operations",
    }
    key = aliases.get(algo_key, algo_key)
    return COMPLEXITY_DATA.get(key, {
        "name": "Unknown Algorithm",
        "best": "-", "average": "-", "worst": "-", "space": "-",
        "note": "No complexity data available."
    })