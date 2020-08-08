
letterMap = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}

sentence = input("Please give me a sentence: ")

for ch in sentence:

    if ch.lower() in letterMap:
        letterMap[ch.lower()] += 1

print(letterMap)

# loop items
# for key, value in letterMap.items():
#     print(key, value)