time_s = int(input("enter time in seconds - "))
base60 = 60
time_m = time_s // base60
if time_s % base60 == 0:
    time_s = 0
else:
    time_s = time_s % base60
time_h = time_m // base60
if time_m % 60 == 0:
    time_m = 0
else:
    time_m = time_m % 60
print("entered time in hh:mm:ss - %02d:%02d:%02d" % (time_h, time_m, time_s))
