"""
score = int(input("ได้คะแนน :"))
grade = ""

def grade(score):
    if score >= 50:
        print("ผ่าน")
        if score >= 50 and score < 55:
            grade = "D"
        elif score >= 55  and score < 60:
            grade = "D+"
        elif score >= 60 and score < 65:
            grade = "C"
        elif score >= 65 and score < 70:
            grade = "C+"
        elif score >= 70  and score < 75:
            grade = "B"
        elif score >= 75  and score < 80:
            grade = "B+"
        else:
            grade = "A"

    else:
        print("ไม่ผ่าน")
    
    print("ได้เกรด" , grade)

grade(score)
"""

x = int(input("ตัวคูณ :"))
y = int(input("คูณถึงไหน :"))
z = 1
i = 1

def Multiply(x , y): 
    global i
    global z
    for i in range(y):
        print(f"{x} * {z} = {x*z}")
        z += 1     

Multiply(x , y)