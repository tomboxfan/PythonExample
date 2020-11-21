
# global variable
total = 0




def fib(n):

    # I am changing a global variable
    global total
    total +=1

    # base case
    if n < 2:
        return n

    # recursive call
    return fib(n-1) + fib(n-2)




print(fib(34))
print(total)
