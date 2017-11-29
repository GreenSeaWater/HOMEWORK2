alphabet_SIZE = 26
values = set(input().lower().replace(' ', ''))

if len(values) == alphabet_SIZE:
    print('pangram')
else:
    print('not pangram')