print("Chương trình nhập dãy số tăng dần")

n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    while True:
        num = int(input(f"Nhập phần tử thứ {i + 1}: "))
        if i == 0 or num > lst[i - 1]:
            lst.append(num)
            break
        else:
            print(" Số vừa nhập phải lớn hơn số trước đó! Vui lòng nhập lại.")

print(" Dãy số tăng dần sau khi nhập là:")
print(lst)