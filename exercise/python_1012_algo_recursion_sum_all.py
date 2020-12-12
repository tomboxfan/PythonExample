def sum_all_no_recursion(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


# sum_all(n) is converted to n + sum_all(n-1)
def sum_all(n):

    # base case:
    if n <= 1:
        return n

    # recursive call
    return n + sum_all(n-1)


# print(sum_all_no_recursion(100))
print(sum_all(100))