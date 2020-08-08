a = ["Apple", 'Orange', 'Banana', "Pear"]

b = a[:]        #['Apple', 'Orange', 'Banana', 'Pear']
c = a[0:6]      #['Apple', 'Orange', 'Banana', 'Pear']
d = a[0:len(a)] #['Apple', 'Orange', 'Banana', 'Pear']

print(b,c,d, sep="\n", end="\n ---------------------------- \n")

e = a

a.append('Rice')       # ["Apple", 'Orange', 'Banana', "Pear", 'Rice']
del a[1]               # ["Apple", 'Banana', "Pear", 'Rice']
a.insert(1, 'Candy')   # ["Apple", 'Candy', 'Banana', "Pear", 'Rice']

print(a, e, sep="\n", end="\n ---------------------------- \n")
print(b,c,d, sep="\n", end="\n ---------------------------- \n")

# value equality
# identity equality

# id()
print(id(a), id(b), id(c), id(d), id(e), sep="\n", end="\n ---------------------------- \n")