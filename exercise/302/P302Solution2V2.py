import math

squareSet = set()
total = 0


# i is the biggest number among the 3
for i in range(1,101):

    squareSet.add(i ** 2)

    # Then I need to find 2 small numbers j and k

    # sqr(j) + sqr(k) = sqr(i)
    # because j < k
    # so, sqr(j) < sqr(i) / 2
    # I just need to loop j to : int(math.sqrt(i ** 2 / 2)) + 1

    for j in range(1, int(math.sqrt(i ** 2 / 2)) + 1):
        sqrNo = i ** 2 - j ** 2
        if sqrNo in squareSet:
            k = int(math.sqrt(sqrNo))
            print(j, k, i)
            total+=1

print("Total:", total)