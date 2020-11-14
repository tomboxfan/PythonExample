

def factorial_no_recursion(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result



# IMPORTANCE!!! --------------------------------------
# 2 important points:
# 1) base case
# 2) recursive call
# ----------------------------------------------------


def factorial(n):

    # base case:
    if n == 1:
        return 1

    # recursive call
    return n * factorial(n-1)


# print(f"factorial of 5 is {factorial_no_recursion(5)}")   # 120
# print(f"factorial of 10 is {factorial_no_recursion(10)}") # 3,628,800
print(f"factorial of 5 is {factorial(5)}")     # 120
print(f"factorial of 10 is {factorial(10)}")   # 3,628,800
