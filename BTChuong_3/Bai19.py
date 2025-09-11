import math

# Hàm tính giá trị biểu thức S(x, n)
def calculate_expression(x, n):
    result = x
    for i in range(1, n + 1):
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result

# Nhập giá trị x và n
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

# Tính và in kết quả
print(f"Giá trị của S({x}, {n}) là: {calculate_expression(x, n)}")
