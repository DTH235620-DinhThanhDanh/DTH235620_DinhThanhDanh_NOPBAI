# Vẽ hình vuông bằng dấu '*'
def draw_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Kích thước hình vuông
size = 5

# Gọi hàm để vẽ hình vuông
draw_square(size)



# Vẽ hình tam giác bằng dấu '*'
def draw_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# Kích thước tam giác
size = 5

# Gọi hàm để vẽ hình tam giác
draw_triangle(size)




# Vẽ hình zigzag bằng dấu '*'
def draw_zigzag(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Kích thước zigzag
size = 5

# Gọi hàm để vẽ hình zigzag
draw_zigzag(size)