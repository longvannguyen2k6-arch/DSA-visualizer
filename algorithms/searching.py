def linear_search(arr, target):
    steps = []
    a = arr.copy()
    n = len(a)

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": f"Searching for target {target} using Linear Search"
    })

    for i in range(n):
        steps.append({
                "state": a.copy(),
                "highlights": [i],
                "action": "compare",
                "description": f"checking index {i}: is {a[i]}=={target}"
            })
        if a[i] == target:
             steps.append({
                    "state": a.copy(),
                    "highlights": [i],
                    "action": "done",
                    "description": f"found target {target} at index {i}"
                        })
             return steps

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "not_found",
        "description": f"Target {target} not found in the array"
    })
    return steps


def binary_search(arr, target):
    steps = []
    a = sorted(arr.copy())
    n = len(a)

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": f"Sorted array for Binary Search. Target: {target}"
    })

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        steps.append({
            "state": a.copy(),
            "highlights":[mid],
            "action":"compare",
            "description":f"Checking middle index {mid} (value {a[mid]}), range [{low}..{high}]"
        })
  

        if a[mid] == target:
            steps.append({
                "state": a.copy(),
                "highlights": [mid],
                "action": "done",
                "description": f"found target {target} at index {mid}"
                        })
        
            return steps
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "not_found",
        "description": f"Target {target} not found in the array"
    })
    return steps