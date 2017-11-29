n = input()
ar = map(int, input().split())
ar = sorted(ar)

diff = ar[1] - ar[0]
for i in range(1, len(ar) - 1):
    if ar[i+1] - ar[i] < diff:
        diff = ar[i + 1] - ar[i]
        result = [ar[i], ar[i + 1]]
    elif ar[i+1] - ar[i] == diff:
        result += [ar[i], ar[i + 1]]
print(*result)