def tinh_toan(a, b, phep_toan):
    if phep_toan == '+':
        return a + b
    elif phep_toan == '-':
        return a - b
    elif phep_toan == '*':
        return a * b
    elif phep_toan == '/':
        if b == 0:
            return "Lỗi: Không thể chia cho 0"
        else:
            return a / b
    else:
        return "Phép toán không hợp lệ"
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")
ket_qua = tinh_toan(a, b, phep_toan)
print("Kết quả:", ket_qua)