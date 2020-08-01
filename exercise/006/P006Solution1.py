i = 0
j = 1

# sep               separator
# \n                next line 换行符
# (i,j, sep='\n')   parameter 参数列表
print(i,j, sep='\n')

for k in range(18):
    next = i + j
    print(next)

    # variable reuse - the difficult part
    i = j
    j = next