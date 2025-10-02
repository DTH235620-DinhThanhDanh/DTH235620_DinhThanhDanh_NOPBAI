from random import randrange

lst = []

print("Nhập số phần tử:")
n = int(input())

# Tạo list ngẫu nhiên
for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# Chèn thêm một số vào list
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# Xóa tất cả các phần tử có giá trị k
k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)

print("List sau khi xóa:")
print(lst)

# Hàm kiểm tra list có đối xứng không
def CheckDoiXung(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

# Kiểm tra và in kết quả
kt = CheckDoiXung(lst)
if kt:
    print("List đối xứng")
else:
    print("List không đối xứng")