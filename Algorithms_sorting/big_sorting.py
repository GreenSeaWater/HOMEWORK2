n = int(input().strip())
d = {}

for i in range(n):
    number = input().strip()
    length = len(number)

    if not length in d:
        d[length] = []
    d[length].append(number)

for key in sorted(d):
    for item in sorted(d[key]):
        print(item)