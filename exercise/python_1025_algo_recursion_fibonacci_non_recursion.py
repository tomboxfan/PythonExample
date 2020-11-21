def fib(n):

    if n == 0:
        return 0

    last = 0
    next = 1

    for _ in range(1, n): # throwaway variable
        last, next = next, last + next # tuple unpacking

    return next

print(fib(35))