'''
In naive recursive algorithm and memorized dynamic programming algorithm
we use recursive algorithm, which means:

if we want to calculate fib(34), then we need to recursively calculate the subproblems to find the final answer.

In bottom-up solution, we work on subproblems first: fib(1), fib(2), fib(3) ....
until we know the answer of fib(n-2) and fib(n-1)
then fib(n) = fib(n-1) + fib(n-2)
This algorithm is called: bottom-up dynamic programming
'''

import time

memory ={0:0,
         1:1}

def fib(n):
    for i in range(n+1):
        if i <= 1:
            value = i
        else:
            value = memory[i-1] + memory[i-2]
        memory[i] = value

    return memory[n]


start = time.time()
print(fib(33))
end = time.time()
total_second = end - start
print(f'It costs {total_second:.2f} seconds.')
