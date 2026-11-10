def recursion_fib(arr):
    n = arr[0] if arr else 5
    n = max(0, min(n, 6))
    steps = []
    call_stack = []

    steps.append({
        "state": [],
        "highlights": [],
        "action": "init",
        "description": f"Calculating Fibonacci({n}) using pure Recursion O(2^n)"
    })

    def _fib(k):
        call_stack.append(f"fib({k})")
        steps.append({
            "state": call_stack.copy(),
            "highlights": [len(call_stack) - 1],
            "action": "push",
            "description": f"Call fib({k}) -> Pushed to Call Stack"
        })

        if k <= 1:
            steps.append({
                "state": call_stack.copy(),
                "highlights": [len(call_stack) - 1],
                "action": "done",
                "description": f"Base case reached: fib({k}) returns {k}"
            })
            call_stack.pop()
            return k

        left = _fib(k - 1)
        right = _fib(k - 2)
        res = left + right

        steps.append({
            "state": call_stack.copy(),
            "highlights": [len(call_stack) - 1],
            "action": "compare",
            "description": f"fib({k}) = fib({k-1}) [{left}] + fib({k-2}) [{right}] = {res}"
        })

        call_stack.pop()
        return res

    result = _fib(n)
    steps.append({
        "state": [f"Result: {result}"],
        "highlights": [0],
        "action": "done",
        "description": f"Recursion completed! Fibonacci({n}) = {result}"
    })
    return steps


def dp_fib(arr):
    n = arr[0] if arr else 6
    n = max(1, min(n, 12))
    steps = []

    dp = ["?"] * (n + 1)
    steps.append({
        "state": dp.copy(),
        "highlights": [],
        "action": "init",
        "description": f"Initialized DP Table of size {n + 1} for Fibonacci({n})"
    })

    dp[0] = 0
    steps.append({
        "state": dp.copy(),
        "highlights": [0],
        "action": "swap",
        "description": "Base case: dp[0] = 0"
    })

    if n >= 1:
        dp[1] = 1
        steps.append({
            "state": dp.copy(),
            "highlights": [1],
            "action": "swap",
            "description": "Base case: dp[1] = 1"
        })

    for i in range(2, n + 1):
        steps.append({
            "state": dp.copy(),
            "highlights": [i - 1, i - 2],
            "action": "compare",
            "description": f"Looking up memoized values: dp[{i-1}] ({dp[i-1]}) + dp[{i-2}] ({dp[i-2]})"
        })
        dp[i] = dp[i - 1] + dp[i - 2]
        steps.append({
            "state": dp.copy(),
            "highlights": [i],
            "action": "swap",
            "description": f"Stored dp[{i}] = {dp[i]} in DP Table"
        })

    steps.append({
        "state": dp.copy(),
        "highlights": [n],
        "action": "done",
        "description": f"DP Bottom-Up completed in O(n) time! Fibonacci({n}) = {dp[n]}"
    })
    return steps