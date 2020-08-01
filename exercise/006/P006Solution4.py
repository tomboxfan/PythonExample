list = [0,1]

# always use the last 2 numbers, plus them, append it
for i in range(18):

    # slicing
    subList = list[-2:]

    list.append(subList[0] + subList[1])

print(list)