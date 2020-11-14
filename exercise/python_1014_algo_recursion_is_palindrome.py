def is_palindrome(str1):

    #base case:
    if len(str1) == 1:
        return True

    #base case:
    if str1[0] != str1[len(str1) - 1]:
        return False

    #recursive call
    return is_palindrome(str1[1:len(str1) - 1])


print(is_palindrome('TENET'))
print(is_palindrome('ABCDADCBA'))
print(is_palindrome('HELLO'))
