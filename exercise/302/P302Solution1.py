import math

total = 0

for i in range(1,101):
    for j in range(i+1, 101):
        k = math.sqrt(i**2 + j**2)
        kInt = int(k)
        if(kInt == k and k <= 100):
            print(i,j,kInt)
            total += 1

print("Total:", total)