n = input()
ar = list(map(int, input().split()))
for i in range(100):
    if i in ar:
        print((str(i) + ' ')*ar.count(i), end='')