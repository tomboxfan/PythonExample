# 然后思考print 3位数，如何print

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            num = i * 100 + j * 10 + k
            print(num)