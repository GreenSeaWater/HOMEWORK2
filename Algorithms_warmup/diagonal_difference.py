n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

d1 = 0
d2 = 0
current_d1 = 0
current_d2 = n - 1
for i in a:
    d1 += int(i[current_d1])
    d2 += int(i[current_d2])

    current_d1 += 1
    current_d2 -= 1
print(abs(d1 - d2))