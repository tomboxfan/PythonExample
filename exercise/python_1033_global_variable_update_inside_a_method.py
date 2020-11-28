# define a global variable x
x = "Hello Python!"

def print_msg():

    # As soon as you say: x = ...
    # Python starts to check: has the variable x been defined in the current scope - print_msg()?
    # No, x is not found in the current scope.
    # So, Python belives: You are defining a new variable.
    # But hang on a second, why you are using x which is not defined at the same time?
    # Python needs to report this bug!
    x = x * 2
    print(x)

print_msg()