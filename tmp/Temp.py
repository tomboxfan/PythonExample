import random

intList = []

for i in range(100):
    intList.append(random.randint(1,1000))

print(intList)
intList.sort()
print(intList)