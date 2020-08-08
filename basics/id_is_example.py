

# id() example --------------------------
a = [1,2,3]
print(id(a))

b = [4,5,6]
print(id(b))

print(" -----------------------------------  ")

b = a

# value equality
print('a == b           :', a == b) # True

# identity equality
print('id(a) == id(b)   :', id(a) == id(b)) # True
print('a is b           :', a is b) # True
print(" -----------------------------------  ")

c = a[:]


# value equality
print('a == c           :', a == c) # True

# identity equality
print('id(a) == id(c)   :', id(a) == id(c)) # False
print('a is c           :', a is c) # False
print(" -----------------------------------  ")


