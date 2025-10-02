def nhap_matrix(m, n, ten="ma trận"):
    print(f"Nhập các phần tử cho {ten} {m}x{n}:")
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"Nhập phần tử [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def xuat_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end='\t')
        print()

def cong_matrix(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def hoan_vi_matrix(M):
    m = len(M)
    n = len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

# Nhập kích thước ma trận
m = int(input("Nhập số dòng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Nhập ma trận A và B
A = nhap_matrix(m, n, "A")
B = nhap_matrix(m, n, "B")

print("\nMa trận A:")
xuat_matrix(A)

print("\nMa trận B:")
xuat_matrix(B)

# Cộng 2 ma trận
C = cong_matrix(A, B)
print("\nMa trận C = A + B:")
xuat_matrix(C)

# Tính ma trận hoán vị
A_T = hoan_vi_matrix(A)
B_T = hoan_vi_matrix(B)

print("\nMa trận hoán vị của A:")
xuat_matrix(A_T)

print("\nMa trận hoán vị của B:")
xuat_matrix(B_T)