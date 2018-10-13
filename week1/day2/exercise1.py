# Interactive Motivator

message = input('Please enter a motivational message: ')
num_times = input('How many times should I repeat the message? ')

for i in range(int(num_times)):
    print(str(i + 1) + '. ' + message)
