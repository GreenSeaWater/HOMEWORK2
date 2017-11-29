def twoStrings(s1, s2):
    for char in s1:
        if char in s2:
            substring = 'YES'
        else:
            substring = 'NO'
    return substring

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)