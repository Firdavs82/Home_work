def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text[])):
            yield text[i: j + i + 1]

a = all_variants('abc')
for i in a:
    print(i)