from random import randrange

# Hàm tạo ma trận ngẫu nhiên m x n
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))  # Tạo số ngẫu nhiên từ 0 đến 99
        D.append(row)
    return D

# Hàm xuất ma trận
def XuatMaTran(D):
    print("Ma trận:")
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# Hàm lấy dòng thứ r trong ma trận D
def LayDong(D, r):
    return D[r]

# Xuất list 1 chiều (dùng cho dòng hoặc cột)
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# Hàm lấy cột thứ c trong ma trận D
def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

# Hàm tìm phần tử lớn nhất trong ma trận
def MAX(D):
    max_value = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] > max_value:
                max_value = D[i][j]
    return max_value

# --- Chương trình chính ---
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)
XuatMaTran(D)

print("Mời bạn nhập dòng muốn xuất (từ 0 đến", m - 1, "):")
r = int(input())
if 0 <= r < m:
    print("Dòng thứ", r, ":")
    XuatList1Chieu(LayDong(D, r))
else:
    print("Dòng không hợp lệ!")

print("Mời bạn nhập cột muốn xuất (từ 0 đến", n - 1, "):")
c = int(input())
if 0 <= c < n:
    print("Cột thứ", c, ":")
    XuatList1Chieu(LayCot(D, c))
else:
    print("Cột không hợp lệ!")

max_val = MAX(D)
print("Số lớn nhất trong ma trận =", max_val)