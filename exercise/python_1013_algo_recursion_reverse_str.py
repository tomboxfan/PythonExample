def reverse_str(str1):

    # base case:
    if len(str1) == 1:
        return str1

    # recursive call:
    return reverse_str(str1[1:]) + str1[0]


print(reverse_str('hello!'))