# 1.1
print('1.1')
for i in range(10):
    print('*' * (i + 1))

print('1.2')
for i in range(10, 0, -1):
    print('*' * i)

print('1.3')
for i in range(1, 11):
    stars = '*' * i
    spaces = ' ' * (20 - (i * 2))
    print(stars + spaces + stars)

print('1.4')
line_index = 1
for i in range(-8, 12):
    if i == -8 or i == 10:
        stars = '*'
    else:
        stars = '*' * line_index * 2
    spaces = ' ' * abs(i - 1)

    # else:
    print(spaces + stars)

    if i <= 0:
        line_index += 1
    elif i >= 0:
        line_index -= 1

print("2")
user_height = input('Please type in a triangle height: ')
print('bottom-heavy triangle')
for i in range(int(user_height)):
    print('*' * (i + 1))

print('top-heavy triangle')
print('1.2')
for i in range(int(user_height), 0, -1):
    print('*' * i)


# Question 3
def print_triangle(height):
    for i in range(height):
        print('*' * (i + 1))


# Question 4
def get_triangle_height():
    user_height = input('Please type in a triangle height: ')
    return int(user_height)


print('5')
height = get_triangle_height()
print_triangle(height)

# Question 6
# Feel free to answer this yourself.
# I found myself spending too much time dealing with symmetry and
# line lengths, so I decided to skip this bonus question.
