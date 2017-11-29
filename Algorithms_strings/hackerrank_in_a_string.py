word = 'hackerrank'
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    n = 0
    if len(word) > len(s):
        print('NO')
        break
    for i in range(len(s)):
        if n < len(word) and s[i] == word[n]:
            n += 1
    if n != 10:
        print('NO')
    else:
        print('YES')