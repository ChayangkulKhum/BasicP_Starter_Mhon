print("ระดับสมาชิก:")
c = input("")
print("ราคาเท่าไร:")
cost = int(input(""))
sale = 0
print("วันที่เท่าไร")
Day = int(input(""))
delivery = 0

if c == "Gold":
    if cost >= 1000:
        sale = cost * 0.15
        if Day % 2 != 0:
            if sale > 500:
                sale + 5/sale
    else:
        sale = cost * 0.1
        if Day % 2 != 0:
            if sale > 500:
                sale + 5/sale

elif c == "Silver":
    if cost >= 1000:
        sale = cost * 0.1
        if Day % 2 != 0:
            if sale > 500:
                sale + 5/sale
    else:
        sale = cost * 0.05
        if Day % 2 != 0:
            if sale > 500:
                sale + (sale * 0.05)
else:
    if Day % 2 != 0:
        sale = cost * 0.05


if cost < 800:
    delivery = 50
else:
    delivery = 0

Total = cost + delivery - sale
print("ราคา:" , cost)
print("ลด" , sale)
print("ค่าส่ง:" , delivery)
print("ต้องจ่าย:" , Total)