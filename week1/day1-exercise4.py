#1
user_str = input("Please enter a string. It must be 10 characters long. ")

#2
print("The first character is '{}'".format(user_str[0]))
print("The last character is '{}'".format(user_str[-1]))

#3
print(user_str[0:1])
print(user_str[0:2])
print(user_str[0:3])
print(user_str[0:4])
print(user_str[0:5])
print(user_str[0:6])
print(user_str[0:7])
print(user_str[0:8])
print(user_str[0:9])
print(user_str[0:10])

#4
mixed = user_str[3:4] + user_str[0:3] + user_str[9] \
    + user_str[7:9] + user_str[4] + user_str[5:7]
print("Here is your string, all mixed up! '{}'".format(mixed))
