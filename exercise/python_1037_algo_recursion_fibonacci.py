
import time

# -------------------------------------
# Naive Recursive Algorithm
# Exponential time
# -------------------------------------



# global variable
total = 0

def fib(n):

    # I am changing a global variable
    global total
    total +=1

    # base case
    if n < 2:
        return n


    # important!!! --------------------------------------------------------------------------------------
    # fibonacci is so classic in recursion algorithm because fib(n) uses the results of 2 sub problems.
    # fib(n) = fib(n-1) + fib(n-2)
    # ---------------------------------------------------------------------------------------------------

    # recursive call
    return fib(n-1) + fib(n-2)



start = time.time()
print(fib(32))
end = time.time()
total_second = end - start
print(f'It costs {total_second:.2f} seconds, with {total:,} method call.')