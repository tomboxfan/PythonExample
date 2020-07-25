x = int(input("Please input x:"))
y = int(input("Please input y:"))
z = int(input("Please input z:"))

# print(x,y,z)

if x < y and y < z:
    print(x, y, z)

elif x < z and z < y:
    print(x, z, y)

elif y < z and z < x:
    print(y, z, x)

elif y < x and x < z:
    print(y, x, z)

elif z < x and x < y:
    print(z, x, y)

elif z < y and y < x:
    print(z, y, x)