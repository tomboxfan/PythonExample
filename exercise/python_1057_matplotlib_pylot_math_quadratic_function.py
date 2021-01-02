
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 201) # [-10, 10] 生成201个点 (分成200段), 所以-10.0, -9.9, -9.8 ....9.9, 10.0 一共201个数字

plt.title("quadratic function: y = x^2")
plt.plot(x, x ** 2)       # y= x^2
plt.plot(x, x ** 3)       # y= x^3
plt.plot(x, x ** 4)       # y= x^4

plt.show()


