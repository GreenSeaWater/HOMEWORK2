def aVeryBigSum(ar):
    ArraySum = 0
    for i in ar:
        ArraySum += i
    return ArraySum

n = int(input().strip())
ar = map(int, input().strip().split(' '))
result = aVeryBigSum(ar)
print(result)