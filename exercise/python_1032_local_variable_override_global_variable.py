

# I define a global variable str_a
str_a = 'Hello Python!' # scope: global



# I define a method with a parameter named str_a
# IMPORTANT!!! All parameters are local variables with the method scope.
def print_msg1(str_a):
    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_as has been defined inside the current scope - print_msg1(str_a)
    # Find it!
    print(f'I am using a local variable "str_a": {str_a}')

print_msg1("Good Day!")


def print_msg2():
    str_a = "Hello Singapore!"
    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_a has been defined inside the current scope - print_msg2()
    # Find it!
    print(f'I am using a local variable "str_a": {str_a}')

print_msg2()


def print_msg3():
    # Python sees you are using variable str_a
    # Firstly, Python tries to see whether str_a has been defined inside the current scope - print_msg3()
    # Nope!
    # Secondly, Python tries to see whether str_a has been defined globally?
    # Find it!
    print(f'I am using a global variable "str_a": {str_a}')

print_msg3()

# GLobal variable is visible everywhere.
print(str_a)