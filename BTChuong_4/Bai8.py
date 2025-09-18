import math

print("Chương trình tính logₐ(x) bằng công thức: logₐ(x) = ln(x) / ln(a)")

try:
    x = float(input("Nhập x: "))
    a = float(input("Nhập a (cơ số): "))

    # Kiểm tra điều kiện hợp lệ
    if x <= 0:
        print("x phải > 0")
    elif a <= 0 or a == 1:
        print("a phải > 0 và a ≠ 1")
    else:
        result = math.log(x) / math.log(a)
        print(f"logₐ({x}) với a = {a} là: {round(result, 5)}")

except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")