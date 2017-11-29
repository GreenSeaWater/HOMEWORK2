n = input()
ar = list(map(int, input().split()))
output = []

for i in range(100):
    output.append(ar.count(i))
print(*output)