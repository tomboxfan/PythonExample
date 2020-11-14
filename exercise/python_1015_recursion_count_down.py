#Requirement: print in console 10 9 8 7 6 5 4 3 2 1

def count_down(n):

    print(n)

    # base case
    if n == 0:
        return

    # recursive call
    count_down(n - 1)


count_down(10)