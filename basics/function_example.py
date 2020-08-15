
# with return value -------------------------------------
def square(x):
    '''
    This function will calculate the square number of the passed-in parameter x
    '''
    return x ** 2;



# without return value -----------------------------------
def launch_missile():
    '''
    This function will launch a missile.
    '''
    print("Missile launched!")



# function with default argument value ----------------------
# User can pass or not pass parameter border
# Parameters who has a default value should be put behind
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)



print(square(10))
launch_missile()

banner("Singapore is a beautiful country")
banner("Singapore is a beautiful country", "*")
