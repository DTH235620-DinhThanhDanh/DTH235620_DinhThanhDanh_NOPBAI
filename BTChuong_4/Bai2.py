from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False

    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đã chọn số [1..100], mời bạn đoán: "))
        print("Bạn đoán lần thứ", solandoan)

        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng! Số máy là =", somay)
            win = True
            break
        elif somay > songuoi:
            print("Bạn đoán sai! Số máy > số bạn đoán.")
        else:
            print("Bạn đoán sai! Số máy < số bạn đoán.")

    if not win:
        print("GAME OVER! Số máy là:", somay)

    hoi = input("Bạn có muốn chơi tiếp không? (bấm 'k' để dừng): ")
    if hoi.lower() == "k":
        break

print("Cám ơn bạn đã chơi Game!")
