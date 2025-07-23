distance = int(input("ระยะทางเท่าไร :"))
Price = 0

if distance<5:
    print("Free")
elif distance >= 5 and distance <= 50:
    print(distance)
    Price = 10
elif distance >= 51 and distance <= 100:
    print(distance)
    Price = 15
elif distance >= 101 and distance <= 300:
    print(distance) 
    Price = 25
elif distance >= 301 and distance <= 500:
    print(distance)
    Price = 35
else:
    print(distance)
    Price = 45

Vat = Price * 0.07
Total = Price + Vat
print(Price)
print(Vat)
print(Total)