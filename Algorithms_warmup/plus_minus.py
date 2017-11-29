n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

ps = 0
ng = 0
zero = 0
for i in arr:
    if i > 0:
        ps += 1
    elif i < 0:
        ng += 1
    else:
        zero += 1

print(ps/n)
print(ng/n)
print(zero/n)