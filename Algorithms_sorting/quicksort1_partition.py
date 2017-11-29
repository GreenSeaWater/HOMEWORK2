def quickSort(list):
    left = []
    right = []
    if len(list) > 1:
        pivot = list[0]
        for i in range(1, len(list)):
            if (list[i] > pivot):
                right.append(list[i])
            else:
                left.append(list[i])
        result = left + [pivot] + right
        for item in result:
            print(item, end=' ')


n = input()
ar = list(map(int,input().split()))
quickSort(ar)