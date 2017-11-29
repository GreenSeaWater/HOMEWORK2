def simpleArraySum(ar):
    return sum(ar)

n = int(input().strip())
ar = map(int, input().strip().split(' '))
result = simpleArraySum(ar)
print(result)