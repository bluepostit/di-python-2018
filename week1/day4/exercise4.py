# We'll use this function later to get a list of integers
# as a comma-separated string.
# Remember: str.join() function only works on a list of strings.
def get_list_as_string(lst):
    return ", ".join(str(x) for x in lst)

# 1 - 3.
user_numbers = []
for i in range(10):
    user_number = input("Please enter a whole number between -100 and 100: ")
    user_numbers.append(int(user_number))

# 4.
print('~' * 40)

# 6.1
print("Your numbers: " + get_list_as_string(user_numbers))
# 6.2
print(f"The sum of all the numbers: {sum(user_numbers)}")
# 6.3
first_and_last = [user_numbers[0], user_numbers[-1]]
print("First and last: " + get_list_as_string(first_and_last))
# 6.4
without_duplicates = sorted(set(user_numbers))
print("Without duplicates: " + get_list_as_string(without_duplicates))
# 6.5
gt50 = [num for num in user_numbers if num > 50]
print("Numbers greater than 50: " + get_list_as_string(gt50))
# 6.6
st10 = [num for num in user_numbers if num < 10]
print("Numbers smaller than 10: " + get_list_as_string(st10))
# 6.7
squares = [num*num for num in user_numbers]
print("Numbers squared: " + get_list_as_string(squares))
# 6.8
# ...
# 6.9
# There are a few ways we can do this. Here is one:
largest = sorted(user_numbers)[-1]
print("The largest number is: {}".format(largest))
# 6.10
# Here is another way:
smallest = min(user_numbers)
print("The smallest number is: {}".format(smallest))
