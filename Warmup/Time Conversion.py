# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

time = input().strip()
hh = time[0:2]
period = time[-2:]
if period.lower() == "am":
    if hh == "12":
        t = "00" + time[2:-2]
    else:
        t = time[0:-2]
else:
    if hh == "12":
        t = time[0:-2]
    else:
        t = str(int(hh) + 12) + time[2:-2]
print(t)
