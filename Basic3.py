distance = int(input("ระยะทางเท่าไร :"))

if distance<5:
    print("Free")
elif distance >= 5 and distance <= 50:
    print(distance)
    print(10)
    print(10 * 0.07)
    print((10 * 0.07)+10)
elif distance >= 51 and distance <= 100:
    print(distance)
    print(15)
    print(15 * 0.07)
    print((15 * 0.07)+15)
elif distance >= 101 and distance <= 300:
    print(distance) 
    print(25)
    print(25 * 0.07)
    print((25 * 0.07)+25)
elif distance >= 301 and distance <= 500:
    print(distance)
    print(35)
    print(35 * 0.07)
    print((35 * 0.07)+35)
else:
    print(distance)
    print(45)
    print(45 * 0.07)
    print((45 * 0.07)+50)
