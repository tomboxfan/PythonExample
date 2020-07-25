x = int(input("Please input x:"))
y = int(input("Please input y:"))
z = int(input("Please input z:"))

# print(x,y,z)

if x < y and x < z and y < z:
    print(x, y, z)

elif x < y and x < z and y > z:
    print(x,z,y)


elif y < x and y < z and x > z:
    print(y, z, x)

elif y < x and y < z and z > x:
    print(y, x, z)


elif z < x and z < y and y > x:
    print(z, x, y)

elif z < x and z < y and x > y:
    print(z, y, x)