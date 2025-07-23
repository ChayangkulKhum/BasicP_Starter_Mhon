"""
x = int(input("เอา x เท่าไร:"))
sum = 0

for i in range(1 , x + 1):
    sum = sum + 5
    print(f"คร้งที่ {i} ได้ผลเป็น"  , sum)


x = int(input("เอา x เท่าไร:"))
i = 1
sum = 0

while i <= x:
    sum = sum + 5
    print(f"ครั้งที่ {i} ได้ผล:" , sum)
    i = i + 1
"""

m_health = 50
sword = 4
bow = 5
axe = 6
i = 1
fighting = 0

#ข้าพเจ้าขออนุญาตใช้ Function เพราะพอผมไม่ใช้ผมงงแล้วมันแก้ยาก 
def ImFighting(m_health , round):
    global i
    while m_health != 0 and i != round+1:
        print("จะใช้อะไรตีมี sword , bow , axe:")
        weapon = input("")
        if weapon == "sword":
            m_health -= sword
        elif weapon == "bow":
            m_health -= bow
        elif weapon == "axe":
            m_health -= axe
        print("Monster เลิอดเหลือ:" , m_health)               

while fighting == 0:
    fight = int(input("ต่อสู้เลือก 1 ถ้าไม่เลือก 2:"))
    if fight == 1:
        round = int(input("จะตีกี่รอบ:")) 
        ImFighting(m_health, round)
        fighting = 1

    elif fight == 2:
        print("คุณหนีได้สำเร็จ")
        break
    
    else:
        print("อะไรของมึงกุให้เลือก 1 กับ 2")

if m_health == 0:
    print("คุณชนะ")
else:
    print("Monster เลือด +20")
    m_health + 20
    ImFighting(m_health, round)
