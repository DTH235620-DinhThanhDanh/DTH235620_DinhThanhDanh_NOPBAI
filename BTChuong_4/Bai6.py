from random import randrange
check_values = [4.5, 34, -1, 100, 0, 99]
possible_values = set(range(0, 100))

print("Kiểm tra các giá trị có thể xuất hiện trong randrange(0, 100):\n")
for value in check_values:
    if isinstance(value, int) and value in possible_values:
        print(f"{value}  Có thể xuất hiện")
    else:
        print(f"{value}  Không thể xuất hiện")