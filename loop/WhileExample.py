c = 5
while c != 0:
    print(c)
    c-=1

c=5
while c:
    print(c)
    c-=1


while True:
    response = input() # input() 从Console 获得输入
    if int(response) % 7 == 0:
        break
    else:
        print(response, "is not a multiple of 7!")