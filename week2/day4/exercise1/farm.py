class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] = self.animals[animal] + count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            if animal not in ['sheep']:
                animal = animal + "s"
            info += f"{animal:15}: {count}\n"
        info += "     E-I-E-I-O!"
        return info

