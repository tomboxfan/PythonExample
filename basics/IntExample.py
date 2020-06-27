
# 2进制，8进制，16进制 ---------------------
i=10
j=0b10 #2
k=0o76 #62
l=0xade #2782
print(i,j,k,l)

# How to construct integer ---------------
a=int()     #0

b=int(2.9)  #2
c=int(2.1)  #2
d=int(-2.9) #-2
e=int(-2.1) #-2
f=int(3.0)  #3
print(a,b,c,d,e,f)

g=int("2") #2
print(g)

# 2进制 / 8进制 / 16进制 转换成 10进制 -----------------------
h=int("10", 2)  #2
i=int("10", 8)  #8
j=int("20", 8)  #16
k=int("10", 16) #16
print(h, i, j, k)
l=int("ff", 16)  #255
print(l)

