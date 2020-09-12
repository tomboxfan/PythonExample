# From Natali
# 采用余数来判断正负号

pi = 0
for i in range(1,10000):
    if i % 2 == 1:
        pi += 4 / (2 * i - 1)
    else:
        pi -= 4 / (2 * i - 1)

print(pi)