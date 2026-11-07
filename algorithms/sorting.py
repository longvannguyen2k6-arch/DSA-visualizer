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

def insertion_sort(arr):
    steps = []
    n = len(arr)
    a = arr.copy()
    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": "initially array"
    })
    for i in range(1, n):
        key = a[i]
        j = i - 1
        steps.append({
            "state": a.copy(),
            "highlights": [i],
            "action": "compare",
            "description": f"Picking key = {key} at index {i}"
        })
        while j >= 0 and a[j] > key:
            steps.append({
                "state": a.copy(),
                "highlights": [j, j + 1],
                "action": "compare",
                "description": f"Comparing {a[j]} > key ({key}), shifting {a[j]} to index {j + 1}"
            })
            a[j + 1] = a[j]
            steps.append({
                "state": a.copy(),
                "highlights": [j, j + 1],
                "action": "swap",
                "description": f"Shifted {a[j]} to index {j + 1}"
            })
            j -= 1
        a[j + 1] = key
        steps.append({
            "state": a.copy(),
            "highlights": [j + 1],
            "action": "swap",
            "description": f"Inserted key {key} at index {j + 1}"
        })
    steps.append({
        "state": a.copy(),
        "highlights": list(range(n)),
        "action": "done",
        "description": "done!"
    })
    return steps

def merge_sort(arr):
    steps = []
    n = len(arr)
    a = arr.copy()

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": "Initial unsorted array"
    })

    def _merge(l, mid, r):
        left_part = a[l : mid + 1]
        right_part = a[mid + 1 : r + 1]
        i = 0      
        j = 0      
        k = l      

        while i < len(left_part) and j < len(right_part):
            steps.append({
                "state": a.copy(),
                "highlights": [l+i,mid+1+j],
                 "action": "compare",
                "description": f"compare between {left_part[i]} and {right_part[j]}"
                            })
            if left_part[i] <= right_part[j]:
                a[k] = left_part[i]
                i += 1
            else:
                a[k] = right_part[j]
                j += 1
            steps.append({
                "state": a.copy(),
                "highlights": [k],
                 "action": "swap",
                "description": f"Placed {a[k]} at index{k}"
                                    })
            k += 1
        while i < len(left_part):
            a[k] = left_part[i]
            steps.append({
                "state": a.copy(),
                 "highlights": [k],
                 "action": "swap",
                "description": f"Placed {a[k]} at index{k}"
                                    })
            i += 1
            k += 1
        while j < len(right_part):
            a[k] = right_part[j]
            steps.append({
                "state": a.copy(),
                "highlights": [k],
                "action": "swap",
                "description": f"Placed {a[k]} at index{k}"
                        })
            j += 1
            k += 1

    def _merge_sort(l, r):
        if l < r:
            mid = (l + r) // 2
            _merge_sort(l, mid)
            _merge_sort(mid + 1, r)
            _merge(l, mid, r)
            
    _merge_sort(0, n - 1)

    steps.append({
        "state": a.copy(),
        "highlights": list(range(n)),
        "action": "done",
        "description": "Array is completely sorted!"
    })
    return steps

def quick_sort(arr):
    steps = []
    n = len(arr)
    a = arr.copy()

    steps.append({
        "state": a.copy(),
        "highlights": [],
        "action": "init",
        "description": "Initial unsorted array"
    })

    def _partition(low, high):
        pivot = a[high] 
        i = low - 1     

        for j in range(low, high):
            steps.append ({
                "state": a.copy(),
                "highlights": [j,high],
                "action": "compare",
                "description": f"compare {a[j]} with pivot {pivot}"
                            })
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps.append({
                    "state": a.copy(),
                    "highlights": [i,j],
                    "action": "swap",
                    "description": f"swap {a[i]} and {a[j]}"
                                        })
        a[i + 1], a[high] = a[high], a[i + 1]
        steps.append({
            "state": a.copy(),
            "highlights": [i+1,high],
            "action": "swap",
            "description": f"Placing pivot {pivot} at its correct index{i+1}"
                                })
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = _partition(low, high)
            _quick_sort(low, pi - 1)   
            _quick_sort(pi + 1, high)  

    
    _quick_sort(0, n - 1)

    steps.append({
        "state": a.copy(),
        "highlights": list(range(n)),
        "action": "done",
        "description": "Array is completely sorted!"
    })
    return steps
