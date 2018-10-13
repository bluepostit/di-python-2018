# 1.1
lst = range(10)
print("1.")
print(*lst)

# 1.2
lst = range(1, 11)
print("2.")
print(*lst)

# 1.3
lst = range(-9, 5)
print("3.")
print(*lst)

# 1.4
lst = range(10, 4, -1)
print("4.")
print(*lst)

# 1.5
lst = range(1, 14, 2)
print("5.")
print(*lst)

# 1.6
lst = []
decimal = 1.5
for index in range(8):
    lst.append(decimal)
    decimal += 0.5
print("6.")
print(*lst)

# 1.7
lst = []
num = 2
for index in range(7):
    lst.append(num)
    num *= 2
print("7.")
print(*lst)

# 2
message = 'Keep Calm and Carry On'
for i in range(3):
    print(message)

# 3
for i in range(3):
    print(str(i + 1) + '. ' + message)