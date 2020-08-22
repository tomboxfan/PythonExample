import math

squareSet = set()
total = 0


# i is the biggest number among the 3
for i in range(1,101):

    squareSet.add(i ** 2)

    # Then I need to find 2 small numbers j and k

    for j in range(1, i):
        sqrNo = i ** 2 - j ** 2
        if sqrNo in squareSet:
            k = int(math.sqrt(sqrNo))

            if k < j:
                print(k, j, i)
                total+=1

print("Total:", total)