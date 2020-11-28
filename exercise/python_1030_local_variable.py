
# local variable local_a is defined inside function example()
# local variable local_a is NOT visible outside the function example()
def example():
    local_a = 'Hello Python!' #scope: example()

    # Python sees you are using variable local_a
    # Firstly, Python tries to see whether local_a has been defined inside the current scope - example()
    # Find it!
    print(local_a)

example()

# local_a is NOT visible outside the function example()
# print(local_a)