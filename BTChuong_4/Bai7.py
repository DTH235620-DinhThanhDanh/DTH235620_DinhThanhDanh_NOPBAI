import math
print("Nhập tọa độ điểm A:")
xA = float(input("xA = "))
yA = float(input("yA = "))
print("Nhập tọa độ điểm B:")
xB = float(input("xB = "))
yB = float(input("yB = "))
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print(f"Độ dài đoạn AB là: {round(AB, 2)}")