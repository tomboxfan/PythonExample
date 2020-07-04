# 最后我想把它放在一个list 中

list = []

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            num = 100 * i + 10 * j + k
            if i != j and i != k and j != k:
                list.append(num)    # append() -> 把num put into list

print("Total number: ", len(list)) # len(list) -> the size of the list

print(list)