print("Chương trình sắp xếp dãy số thực theo thứ tự giảm dần")

n = int(input("Nhập số lượng phần tử: "))
M = []

# Nhập dãy số thực
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)

# Xuất kết quả
print(" Dãy số sau khi sắp xếp giảm dần:")
for i in range(n):
    print(f"M[{i}] = {M[i]}")