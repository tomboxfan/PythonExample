
# from 100 to 999
for i in range(100, 1000):

    # // 取整
    # % 取余
    # 213 // 100 == 2
    # 213 % 100 == 13

    a = i // 100
    b = i % 100 // 10
    c = i % 10

    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)