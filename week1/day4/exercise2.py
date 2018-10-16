birthdays = {
    'Albert Einstein': '1879/03/14',
    'W. A. Mozart': '1756/01/27',
    'Isaac Newton': '1643/01/04',
    'Richard Dawkins': '1941/03/26',
    'Jimi Hendrix': '1942/11/27'
}

print("Welcome to the birthday library! "
      "You can look up the birthday of the people in the list")
names = sorted(birthdays.keys())
print(f"We have birthday information for: {', '.join(names)}")

name = (input("Which person's birthday do you want to see? ")
        .strip().title())
if name not in birthdays:
    print(f"Sorry, we don't have birthday information for {name}")
else:
    birthday = birthdays[name.title()]
    print(f"{name}'s birthday is on {birthday}")

