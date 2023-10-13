time_zone = int(input("Enter time zone: "))
london_time = 10.5
if time_zone + london_time > 24:
    print("Wednesday")
elif time_zone + london_time >= 0:
    print("Tuesday")
else:
    print("Monday")