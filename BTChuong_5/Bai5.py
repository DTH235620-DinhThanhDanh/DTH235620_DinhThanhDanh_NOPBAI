def is_vowel(ch):
    return ch.lower() in 'aeiou'

def analyze_string(s):
    in_hoa = 0
    in_thuong = 0
    so = 0
    ky_tu_dac_biet = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0

    for ch in s:
        if ch.isupper():
            in_hoa += 1
        if ch.islower():
            in_thuong += 1
        if ch.isdigit():
            so += 1
        if ch.isspace():
            khoang_trang += 1
        if not ch.isalnum() and not ch.isspace():
            ky_tu_dac_biet += 1
        if ch.isalpha():
            if is_vowel(ch):
                nguyen_am += 1
            else:
                phu_am += 1

    print("\nPhân tích chuỗi:")
    print("Số chữ IN HOA:", in_hoa)
    print("Số chữ in thường:", in_thuong)
    print("Số chữ số:", so)
    print("Số ký tự đặc biệt:", ky_tu_dac_biet)
    print("Số khoảng trắng:", khoang_trang)
    print("Số nguyên âm:", nguyen_am)
    print("Số phụ âm:", phu_am)

import re

def NegativeNumberInStrings(s):
    # Dùng regex để tìm các số âm (ví dụ: -12, -3, -10.5)
    pattern = r'-\d+(\.\d+)?'
    matches = re.findall(pattern, s)
    # Chuyển chuỗi số âm sang float hoặc int nếu cần
    result = re.findall(r'-\d+(?:\.\d+)?', s)
    return result
#chay chuong trinh
chuoi = input("Nhập vào một chuỗi bất kỳ: ")
analyze_string(chuoi)

so_am_trong_chuoi = NegativeNumberInStrings(chuoi)
print("\nCác số âm trích được trong chuỗi:", so_am_trong_chuoi)