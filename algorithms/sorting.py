def bubble_sort(arr):
    steps = []
    n = len(arr)
    a = arr.copy()
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": "initially array"
    })
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                "state": a.copy(),
                "highlights": [j, j + 1],
                "action": "compare",
                "description": f"Comparing {a[j]} and {a[j + 1]}"
            })

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps.append({
                    "state": a.copy(),
                    "highlights": [j, j + 1],
                    "action": "swap",
                    "description": f"swap {a[j + 1]} and {a[j]} because {a[j + 1]} > {a[j]}"
                })
    steps.append({
        "state": a.copy(),
        "highlights": list(range(n)),
        "action": "done",
        "description": "done!"
    })
    return steps
