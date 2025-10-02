def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Nhập mảng (có thể sửa bằng input nếu cần)
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Dòng 1: Số lẻ
so_le = [x for x in M if x % 2 != 0]
print("Số lẻ:", ', '.join(str(x) for x in so_le), f"({len(so_le)} số lẻ)")

# Dòng 2: Số chẵn
so_chan = [x for x in M if x % 2 == 0]
print("Số chẵn:", ', '.join(str(x) for x in so_chan), f"({len(so_chan)} số chẵn)")

# Dòng 3: Số nguyên tố
so_nt = [x for x in M if is_prime(x)]
print("Số nguyên tố:", ', '.join(str(x) for x in so_nt), f"({len(so_nt)} số nguyên tố)")

# Dòng 4: Không phải số nguyên tố
khong_nt = [x for x in M if not is_prime(x)]
print("Không phải nguyên tố:", ', '.join(str(x) for x in khong_nt), f"({len(khong_nt)} số)")