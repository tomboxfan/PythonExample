# Creat a list ------------------------------------

a = ["Apple", 'Orange', 'Banana', "Pear"]
print(a)
print(a[1])
print(len(a))

b = ['tiger',
     'elephant',
     'snake',
     'shark']
print(b)

c = list("I love python!")
print(c)


# List can be heterogeneous (Contains all kinds of objects)
a[1] = 7
a.append([1, 2, 3])
a.append(1.234)
a.append('Sunday')
a.append(True)
a.append(0xf)
print(a)

fruits = ["Pear", 'Orange', 'Banana', "Apple"]

#list.pop(index)
fruit1 = fruits.pop(0)
fruit2 = fruits.pop(1)
print(fruit1) # Pear
print(fruit2) # Banana
print(fruits) # ['Orange', 'Apple']


fruits = ["Pear", 'Orange', "Pear", 'Banana', "Apple"]

#list.remove(value)
fruits.remove("Pear")
print(fruits)  # ['Orange', 'Pear', 'Banana', 'Apple']

fruits.remove("Pear")
print(fruits)  # ['Orange', 'Banana', 'Apple']




#sort fruits
fruits.sort()
print(fruits)



