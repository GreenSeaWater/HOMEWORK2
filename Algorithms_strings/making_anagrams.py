from collections import Counter

def makingAnagrams(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    diff = (d1 - d2) + (d2 - d1)

    return sum(diff.values())


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)