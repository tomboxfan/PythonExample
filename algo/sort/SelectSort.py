import random

intList = []

for i in range(100):
    intList.append(random.randint(1,1000))

print("Before Sort", intList)


for i in range(len(intList)):

    # first I want to define, where is the smallest number
    candidateIndex = i

    # I need to find the smallest number in the remaining numbers
    # For example: For No1. where is the smallest number in the remaining 9 numbers?
    # For example: For No2. where is the smallest number in the remaining 8 numbers?
    # For example: For No3. where is the smallest number in the remaining 7 numbers?
    for j in range(i+1, len(intList)):
        if intList[j] < intList[candidateIndex]:
            candidateIndex = j

    # swap numbers
    intList[candidateIndex],intList[i] = intList[i],intList[candidateIndex]




print("After sort", intList)