def timeConversion(s):
    time = s.strip('AMP').split(':')
    hh, mm, ss = map(int, time)

    if ("PM" in s) and hh != 12:
        hh += 12
    if ("AM" in s) and (hh == 12):
        hh = 0
    return '%(hh)02d:%(mm)02d:%(ss)02d' % {"hh": hh, "mm": mm, "ss": ss}

s = input().strip()
result = timeConversion(s)
print(result)