def ToiUuChuoi(s):
    s2 = s.strip()  # Bỏ khoảng trắng đầu và cuối
    arr = s2.split(' ')  # Tách chuỗi thành mảng các từ (có thể có phần tử rỗng nếu có nhiều dấu cách)
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:  # Bỏ qua phần tử rỗng
            s2 = s2 + word + " "
    return s2.strip()  # Trả về chuỗi đã tối ưu, bỏ dấu cách cuối

s = "   Đinh   Thanh    Danh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))