import random

# We'll use this function later to get a list of integers
# as a comma-separated string.
# Remember: str.join() function only works on a list of strings.
def get_list_as_string(lst):
    return ", ".join(str(x) for x in lst)

# Generate random integers between 11 and 50.
# The question asks for > 50, but I changed it here for convenience.
amt_integers = random.randint(11, 50)
integers = []
for i in range(amt_integers):
    rand_int = random.randint(-100, 100)
    integers.append(rand_int)

# 4.
print('~' * 40)

# 6.1
print("Your numbers: " + get_list_as_string(integers))
# 6.2
print(f"The sum of all the numbers: {sum(integers)}")
# 6.3
first_and_last = [integers[0], integers[-1]]
print("First and last: " + get_list_as_string(first_and_last))
# 6.4
without_duplicates = sorted(set(integers))
print("Without duplicates: " + get_list_as_string(without_duplicates))
# 6.5
gt50 = sorted([num for num in integers if num > 50])
print("Numbers greater than 50: " + get_list_as_string(gt50))
# 6.6
st10 = sorted([num for num in integers if num < 10])
print("Numbers smaller than 10: " + get_list_as_string(st10))
# 6.7
squares = [num*num for num in integers]
print("Numbers squared: " + get_list_as_string(squares))
# 6.8
# ...
# 6.9
# There are a few ways we can do this. Here is one:
largest = sorted(integers)[-1]
print("The largest number is: {}".format(largest))
# 6.10
# Here is another way:
smallest = min(integers)
print("The smallest number is: {}".format(smallest))
