
import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-10, 10, 0.1) # [-10, 10) 每个0.1产生一个数字 (不包括10), 所以-10.0, -9.9, -9.8 ....9.9 一共200个数字
x = np.linspace(-10, 10, 201) # [-10, 10] 生成201个点 (分成200段), 所以-10.0, -9.9, -9.8 ....9.9, 10.0 一共201个数字

# print(type(x))
# print(x)

y = x * 2

# print(type(y))
# print(y)

plt.title("linear function: y = 2x")
plt.plot(x, y)       # y= 2x
plt.plot(x, x * 4)   # y = 4x
plt.plot(x, x * 8)   # y = 8x

plt.show()


