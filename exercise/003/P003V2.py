import math

# variable defintion - define i
for i in range(-100, 10000):
    a = i + 100
    b = a + 168

    aSqrt = math.sqrt(a)
    aSqrtInt = int(aSqrt)

    if aSqrt != aSqrtInt:
        continue  # continue to next loop. It means, i+1, go to line 5

    bSqrt = math.sqrt(b)
    bSqrtInt = int(bSqrt)

    if bSqrt != bSqrtInt:
        continue  # continue to next loop. It means, i+1, go to line 5

    print(i, "is such a number!")