def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
#Truonghop1
def main():
    global val
    val = 5
    print(sum1(5))  # sum1 dùng n=5
    print(sum2())    # sum2 thay đổi val từ 5 xuống 0
    print(sum3())    # sum3 dùng val = 0 (đã bị sum2 thay đổi)
main()
#Truonghop2
def main():
    global val
    val = 5
    print(sum1(5))  # 5
    print(sum3())    # sum3 dùng val = 5, không thay đổi val
    print(sum2())    # sum2 thay đổi val từ 5 xuống 0
main()
#Truonghop3
def main():
    global val
    val = 5
    print(sum2())    # sum2 thay đổi val từ 5 xuống 0
    print(sum1(5))   # sum1 dùng n=5, không liên quan val
    print(sum3())    # sum3 dùng val=0 (đã bị sum2 thay đổi)
main()
