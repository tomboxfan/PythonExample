list = [0,1]

# always use the last 2 numbers, plus them, append it
for i in range(18):
    list.append(list[-1] + list[-2])

print(list)