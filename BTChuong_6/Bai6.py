from random import sample

print("Chương trình tạo list ngẫu nhiên KHÔNG TRÙNG NHAU")
n = int(input("Nhập số phần tử: "))

# Tạo list gồm n số ngẫu nhiên không trùng nhau trong khoảng [-100, 100]
# Khoảng phải đủ lớn (ít nhất n số). [-100, 100] có 201 số.

if n > 201:
    print("Không thể tạo list với", n, "số KHÔNG TRÙNG trong khoảng [-100, 100]")
else:
    lst = sample(range(-100, 101), n)
    print("List ngẫu nhiên không trùng nhau là:")
    print(lst)