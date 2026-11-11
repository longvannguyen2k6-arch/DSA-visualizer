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
def sliding_window(arr, k):
    steps = []
    a = arr.copy()
    n = len(a)
    if k <= 0 or k > n:
        k = min(3, n)

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": f"Sliding Window (size K={k}): Finding max sum of {k} consecutive elements"
    })

    if n == 0:
        return steps

    window_sum = sum(a[:k])
    max_sum = window_sum
    max_start = 0

    steps.append({
        "state": a.copy(),
        "highlights": list(range(0, k)),
        "action": "compare",
        "description": f"Initial window [0..{k-1}] sum = {window_sum} (Max sum = {max_sum})"
    })

    for i in range(k, n):
        entering = a[i]
        leaving = a[i - k]
        prev_sum = window_sum
        window_sum = prev_sum - leaving + entering

        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1

        steps.append({
            "state": a.copy(),
            "highlights": list(range(i - k + 1, i + 1)),
            "action": "compare",
            "description": f"Slide window to [{i-k+1}..{i}]: {prev_sum} - {leaving} + {entering} = {window_sum} (Max = {max_sum})"
        })
    steps.append({
        "state": a.copy(),
        "highlights": list(range(max_start, max_start + k)),
        "action": "done",
        "description": f"Done! Max sum is {max_sum} at subarray {a[max_start : max_start + k]} (indices {max_start}..{max_start + k - 1})"
    })
    return steps


def two_pointers(arr, target):
    steps = []
    a = sorted(arr.copy())
    n = len(a)

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": f"Two Pointers on sorted array: Finding pair with sum == {target}"
    })

    left = 0
    right = n - 1

    while left < right:
        curr_sum = a[left] + a[right]

        steps.append({
            "state": a.copy(),
            "highlights": [left, right],
            "action": "compare",
            "description": f"Left[{left}] ({a[left]}) + Right[{right}] ({a[right]}) = {curr_sum} (Target = {target})"
        })

        if curr_sum == target:
            steps.append({
                "state": a.copy(),
                "highlights": [left, right],
                "action": "done",
                "description": f"Found pair! {a[left]} (idx {left}) + {a[right]} (idx {right}) == {target}"
            })
            return steps
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "not_found",
        "description": f"No pair found with sum equal to {target}"
    })
    return steps