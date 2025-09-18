import math

print("Chương trình tính căn bậc 2 lồng nhau")

try:
    x = float(input("Nhập x (x ≥ 0): "))
    n = int(input("Nhập số lần lồng căn (n ≥ 1): "))

    if x < 0 or n < 1:
        print("x phải ≥ 0 và n phải ≥ 1")
    else:
        result = 0
        for _ in range(n):
            result = math.sqrt(x + result)

        print(f"Kết quả căn bậc 2 lồng nhau {n} lần là: {round(result, 6)}")

except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số.")