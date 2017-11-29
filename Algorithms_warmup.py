####################################################### SOLVE ME FIRST ################################################################

def solveMeFirst(a,b):
    return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)


###################################################### SIMPLE ARRAY SUM ################################################################

def simpleArraySum(n, ar):
    ArraySum = 0
    for i in range(len(ar)):
        ArraySum += ar[0]
        ar.remove(ar[0])
    return ArraySum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)


########################################################### COMPARE THE TRIPLETS ##########################################################

def solve(a0, a1, a2, b0, b1, b2):
    A = 0
    B = 0
    if a0 > b0:
        A += 1
    elif a0 < b0:
        B += 1

    if a1 > b1:
        A += 1
    elif a1 < b1:
        B += 1

    if a2 > b2:
        A += 1
    elif a2 < b2:
        B += 1
    return A, B


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))


######################################################### A VERY BIG SUM #############################################################

def aVeryBigSum(n, ar):
    ArraySum = 0
    for i in range(len(ar)):
        ArraySum += ar[0]
        ar.remove(ar[0])
    return ArraySum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)


######################################################## DIAGONAL DIFFERENCE #######################################################

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


############################################################### PLUS MINUS #############################################################

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


###################################################### STAIRCASE #################################################################

n = int(input().strip())
for i in range(1, n+1):
    print(('#'*i).rjust(n, ' '))


########################################################### MINI-MAX SUM #########################################################

arr = list(map(int, input().strip().split(' ')))
x = sum(arr)
print(x-(max(arr)), x-(min(arr)))


######################################################### BIRTHDAY CAKE CANDLES #####################################################

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)


####################################################### TIME CONVERSION #########################################################

from time import strptime, strftime
def timeConversion(s):
    return strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p"))

s = input().strip()
result = timeConversion(s)
print(result)

























