'''
动态规划
Memorized Dynamic Programming Algorithm
'''


import time

total = 0

memory = {0:0,
          1:1}


def fib(n):

    global total
    total += 1

    # base case
    if n <= 1:
        return n

    #recursive call
    if n not in memory:
        memory[n] = fib(n-1) + fib(n-2)

    return memory[n]



start = time.time()
print(fib(33))
end = time.time()
total_second = end - start
print(f'It costs {total_second:.2f} seconds, with {total:,} method call.')

# IMPORTANT !!! -----------------------------------------
# Summary: What is dynamic programming?
# 1) subproblems + 'Reuse'
# 2) Recursion + memorization
#
# Basic steps:
# 1) take a problem
# 2) split it into subproblems
# 3) solve those subproblems
# 4) reuse the solutions/answers
# -------------------------------------------------------