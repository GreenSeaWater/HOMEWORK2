s = input().strip()
count = 1
for i in s:
    if i.isupper() == True:
        count += 1
print(count)