# Vincent
# 简洁就是美！
# 使用了 -1的次方操作。奇数次方是负数，偶数次方是正数。

pi = 0

for i in range(10000):
    pi += 4/(1 + i * 2) * ((-1) ** i)

print(pi)