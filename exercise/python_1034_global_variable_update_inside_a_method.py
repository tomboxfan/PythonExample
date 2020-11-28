# define a global variable x
x = "Hello Python!"

def print_msg():

    # global x tells Python:
    # I am NOT defining any variable.
    # x is a variable with scope global
    global x


    # As soon as you say: x = ...
    # Python starts to check: has the variable x been defined in the current scope - print_msg()?
    # OH! x is a global variable already defined, not in this scope - print_msg()
    # So you are trying to update the global variable. No problem!
    x = x * 2
    print(x)

print_msg()

# Global variable x has been updated..
print(x)
