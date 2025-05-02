#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

sensor_threshold = int(input("How much daylight is there outside right now? (1-15) "))

if sensor_threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")