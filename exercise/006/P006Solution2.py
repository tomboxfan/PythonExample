list = [0,1]

# #append index 2
# list.append( list[0] + list[1]) -> append list[2]
#
# #append index 3
# list.append( list[1] + list[2]) -> append list[3]
#
# #append index 4
# list.append( list[2] + list[3]) -> append list[4]

for i in range(18):
    list.append(list[i] + list[i+1])

print(list)