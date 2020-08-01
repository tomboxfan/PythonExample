
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

# indexing example --------
print(a[0]) # spam
print(a[2]) # bacon
print(a[5]) # lobster

print(a[-1]) # lobster
print(a[-2]) # ham
print(a[-5]) # egg
print(a[-len(a)]) # spam

# slicing example -----------
# 切片 - subList - 子串
print(a[1:4]) # ['egg', 'bacon', 'tomato']
print(a[2:5]) # ['bacon', 'tomato', 'ham']
print(a[-5:-2]) # ['egg', 'bacon', 'tomato']

print(a[:4]) # = a[0:4]      ['spam', 'egg', 'bacon', 'tomato']
print(a[2:]) # = a[2:len(a)] ['bacon', 'tomato', 'ham', 'lobster']
print(a[:])  # = a[0:len(a)] ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

# step parameter
print(a[1:4:2]) # 表示 a[1:4]的结果(['egg', 'bacon', 'tomato']) 我只要偶数，奇数不要. ['egg', 'tomato']
print(a[1:4:4]) # 表示 a[1:4]的结果(['egg', 'bacon', 'tomato']) 我只要4的倍数，其它不要. ['egg']
print(a[::3])   # ['spam', 'tomato']



