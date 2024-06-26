#Writ a program to get remaining time hours, minutes, and seconds of the day

#
# Expected Output:
# Enter time: 10:15
# ------------ Remaining Time ----------------------
#Hours = 7.5 Hours
#Minutes =
#Seconds

time = input("Enter TIme in HH:MM Format")
hh = int (time[0:2])
mm = int(time[3:])

print(hh)
print(mm)

hours_remaining = (24 - hh)
minutes_remaining = (60 - mm)
seconds


print("------------ Remaining Time ----------------------")
print("Hours = " + str(hours_remaining))
print("Minutes = " + str(minutes_remaining))






