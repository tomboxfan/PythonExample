import math

print('hello world')
print('hello', 'world')

first = 'James'
last = 'Bond'
# last = 'Billy'
age = 90


# example of % ----------------------------------------------------------

# use variable 'last' in your message

# %     speparate messages from parameter list
#       message % parameter list
# %s    str variable
message = 'No, Mr. %s, I expect you to die' % last
print(message)

# %d    int variable
print('Sean Connery is now %d years old' % age)

# %f    float variable
print('pi: %f' % math.pi)

# Here we use 2 float variables, both values are math.pi
# %0.2f     2 digits after decicmal points
print('pi: %f\nshort pi %0.2f' % (math.pi, math.pi))


# example of {} ----------------------------------------------------------

# f开头       This is a format message
print(f'The name is {last}, {first} {last}') # The name is Bond, James Bond
print(f"Sean's age times pi is {age * math.pi}") # 90 * 3.141593 = 282.7433388230814


# sep
print('there are', 6, 'apples in the basket')
print('there are', 6, 'apples in the basket', sep='\n')
print('there are', 6, 'apples in the basket', sep='\U0001f604')
