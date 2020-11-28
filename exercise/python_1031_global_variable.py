
# variable global_a is not defined inside anything, so it is a global variable
# variable global_a is visible everywhere

global_a = "Hello Python!"

def example():

    # Python sees you are using variable global_a
    # Firstly, Python tries to see whether global_a has been defined inside the current scope - example()
    # Nope!
    # Secondly, Python tries to see whether global_a has been defined globally?
    # Find it!
    print(global_a)

example()

print(global_a)
