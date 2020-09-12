# Yifan
# 同样使用了 -1的次方操作。奇数次方是负数，偶数次方是正数。

# Yifan 使用了2种算法来实现。除了for loop，还有while loop
# 这个关于while loop的算法，是非常巧妙的。因为我们在实际运算中，真实的输入值，可能只是pi值得误差值
# 没有人会告诉你，到底要loop多少次
# 所以使用while loop 绝对要打败所有for loop的算法

pi = 0
i = 0

while True:
    pi += 4/(1 + i * 2) * ((-1) ** i)
    i += 1

    #Yifan特有的, 同时她在第7行，放了一个很大的数字
    if 4/(1 + i * 2) < 0.000001:
        break

print(pi)