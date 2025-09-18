def oscillate():
    result = []
    for i in range(-3, 5):  # từ -3 đến 4
        result.append(str(i))
        result.append(str(-i))
    return ' '.join(result)

print(oscillate())