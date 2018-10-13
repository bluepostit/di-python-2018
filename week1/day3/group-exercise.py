fav_fruits = input('Please enter your favourite fruits. ' \
    'Separate multiple items with a space: ')

fav_fruits_lst = fav_fruits.split()

fruit = input('Please type the name of a fruit: ')
if fruit not in fav_fruits_lst:
    print("Are you sure? You really like " + fav_fruits)
else:
    print("You like those! Good choice!")
