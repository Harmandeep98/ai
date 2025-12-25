device = True;
temp = 38;

if not device:
    print("Device is off");
else:
    print("Device is on");
    if temp > 37:
        print("Temperature is too high");
    elif temp == 37:
        print("Temperature is just right");
    else:
        print("Temperature is too low");