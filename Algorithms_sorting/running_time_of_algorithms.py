def insertion_sort(ar):
    count = 0
    for i in range(1, len(ar)):
        j = i - 1
        temp = ar[i]
        while ar[j] > temp and j >= 0:
            ar[j + 1] = ar[j]
            count += 1
            j -= 1

        ar[j + 1] = temp
    return count


m = input()
ar = list(map(int, input().split()))
print(insertion_sort(ar))