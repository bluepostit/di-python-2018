import random

DEBUG = False


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    throws = []
    has_doubles = False
    while not has_doubles:
        throw1 = throw_dice()
        throw2 = throw_dice()
        has_doubles = (throw1 == throw2)
        throws.append((throw1, throw2))
    if DEBUG:
        print("I threw {} times until I got doubles.".format(len(throws)))
        print(*throws)
    return len(throws)


throws_until_doubles = []
for i in range(100):
    throws = throw_until_doubles()
    throws_until_doubles.append(throws)

if DEBUG:
    print(*throws_until_doubles)
print("I threw until doubles 100 times.")
print("This took {} throws".format(sum(throws_until_doubles)))
print("Average amount of times until I got doubles: {}"
      .format(sum(throws_until_doubles) / 100))
