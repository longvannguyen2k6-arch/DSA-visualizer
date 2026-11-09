def stack_operations(arr):
    steps = []
    stack = []

    steps.append({
        "state": [],
        "highlights": [],
        "action": "init",
        "description": "Initialized empty Stack (LIFO - Last In, First Out)"
    })

   
    for val in arr:
        stack.append(val)
        steps.append({
            "state": stack.copy(),
            "highlights": [len(stack) - 1],
            "action": "push",
            "description": f"Push({val}): Added {val} to the top of the stack"
        })

    if stack:
        steps.append({
            "state": stack.copy(),
            "highlights": [len(stack) - 1],
            "action": "compare",
            "description": f"Peek(): Top element is {stack[-1]} (index {len(stack) - 1})"
        })

       
        popped = stack.pop()
        steps.append({
            "state": stack.copy(),
            "highlights": [len(stack) - 1] if stack else [],
            "action": "pop",
            "description": f"Pop(): Removed {popped} from the top of the stack"
        })

    steps.append({
        "state": stack.copy(),
        "highlights": list(range(len(stack))),
        "action": "done",
        "description": "Stack demonstration completed!"
    })
    return steps
def queue_operations(arr):
    steps = []
    queue = []

    steps.append({
        "state": [],
        "highlights": [],
        "action": "init",
        "description": "Initialized empty Queue (FIFO - First In, First Out)"
    })
    for val in arr:
        queue.append(val)
        steps.append({
            "state": queue.copy(),
            "highlights": [len(queue) - 1],
            "action": "enqueue",
            "description": f"Enqueue({val}): Added {val} to the rear of the queue"
        })

    if queue:
        steps.append({
            "state": queue.copy(),
            "highlights": [0],
            "action": "compare",
            "description": f"Front(): First element in line is {queue[0]} (index 0)"
        })

        dequeued = queue.pop(0)
        steps.append({
            "state": queue.copy(),
            "highlights": [0] if queue else [],
            "action": "dequeue",
            "description": f"Dequeue(): Removed {dequeued} from the front of the queue"
        })

    steps.append({
        "state": queue.copy(),
        "highlights": list(range(len(queue))),
        "action": "done",
        "description": "Queue demonstration completed!"
    })
    return steps
def linked_list_operations(arr):
    steps = []
    ll = []

    steps.append({
        "state": [],
        "highlights": [],
        "action": "init",
        "description": "Initialized empty Singly Linked List (HEAD -> NULL)"
    })

    for val in arr:
        ll.append(val)
        steps.append({
            "state": ll.copy(),
            "highlights": [len(ll) - 1],
            "action": "insert",
            "description": f"Insert({val}): Created node [{val}] and linked at the tail"
        })

    for i, val in enumerate(ll):
        steps.append({
            "state": ll.copy(),
            "highlights": [i],
            "action": "compare",
            "description": f"Traverse: Visiting node [{val}] at position {i}"
        })

    if ll:
        deleted = ll.pop(0)
        steps.append({
            "state": ll.copy(),
            "highlights": [0] if ll else [],
            "action": "delete",
            "description": f"DeleteHead(): Removed node [{deleted}], updated HEAD pointer"
        })

    steps.append({
        "state": ll.copy(),
        "highlights": list(range(len(ll))),
        "action": "done",
        "description": "Linked List operations completed!"
    })
    return steps