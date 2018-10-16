# The '\'' character at the beginning of a multi-line string
# tells Python to ignore the first line of the string, and
# start on the next line (line 4 in this case)
cars_str = '''\
Acura
Alfa Romeo
Aston Martin
Audi
Bentley
BMW
Bugatti
Buick
Cadillac
Chevrolet
Chrysler
Citroen
Dodge
Ferrari
Fiat
Ford
Geely
General Motors
GMC
Honda
Hyundai
Infiniti
Jaguar
Jeep
Kia
Koenigsegg
Koenigsegg
Lamborghini
Land Rover
Lexus
Maserati
Mazda
McLaren
Mercedes-Benz
Mini
Mitsubishi
Nissan
Pagani
Pagani
Peugeot
Porsche
Ram
Renault
Rolls Royce
Saab
Saab
Subaru
Suzuki
TATA Motors
Tata Motors
Tesla
Toyota
Volkswagen
Volvo'''

# Get rid of white space with strip()
cars = cars_str.strip().split('\n')
# There is a built-in Python function to do this, too:
# cars = cars_str.splitlines()
print(f'There are {len(cars)} manufacturers in the list')

# Remove duplicates and sort
cars = sorted(set(cars))
print('Manufacturers: ')
print(', '.join(cars))
print()

# Print the list in reverse
cars_reversed = []
for i in range(len(cars) - 1, 0, -1):
    cars_reversed.append(cars[i])
print('Manufacturers in reverse order:')
print(', '.join(cars_reversed))
print()

# With the letter 'o' in their name
with_o = [car for car in cars if 'o' in car.lower()]
print(f'{len(with_o)} manufacturers have the letter \'o\'')

# Without the letter 'i' in their name
without_i = [car for car in cars if 'i' not in car.lower()]
print(f'{len(without_i)} manufacturers do not have the letter \'i\'')
