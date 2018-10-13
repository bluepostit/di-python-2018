

# 1.1, 1.2, 1.3
def first_version():
    sex = input('Please enter your sex (m/f): ')
    date_of_birth = input("Please enter your date of birth \
in the form 'YYYY/MM/DD': ")

    dob_list = date_of_birth.split('/')
    year_of_birth = int(dob_list[0])
    age = 2018 - year_of_birth
    print("You are {} years old.".format(age))


# 1.4, 1.5
def get_age(date_of_birth):
    dob_list = date_of_birth.split('/')
    year_of_birth = int(dob_list[0])
    age = 2018 - year_of_birth
    return age


def can_retire(sex, date_of_birth):
    if sex in ['m', 'M']:
        retirement_age = 67
    else:
        retirement_age = 62
    age = get_age(date_of_birth)
    if age >= retirement_age:
        return True
    else:
        return False

sex = input('Please enter your sex (m/f): ')
date_of_birth = input("Please enter your date of birth \
in the form 'YYYY/MM/DD': ")
print("You are {} years old.".format(get_age(date_of_birth)))
if can_retire(sex, date_of_birth):
    print("Good work. You can now retire.")
else:
    print("You can't retire just yet. Keep on working")
