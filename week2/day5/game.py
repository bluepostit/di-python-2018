from random import randint


class Game:

    def get_user_item(self):
        while True:
            user_item = (input("Select (r)ock, (p)aper, or (s)cissors: ")
                         .strip().lower())
            if user_item not in ['r', 'p', 's']:
                print("Invalid input. Please try again")
            else:
                return user_item

    def get_computer_item(self):
        rand = randint(0, 2)
        items = ['r', 'p', 's']
        return items[rand]

    def get_game_result(self, user_item, computer_item):
        """Get the game results, comparing the two items."""
        if user_item == computer_item:
            return 'draw'
        elif ((user_item == 'r' and computer_item == 's')
              or (user_item == 'p' and computer_item == 'r')
              or (user_item == 's' and computer_item == 'p')):
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item)
        print("You chose: {}. The computer chose: {}. Result: {}"
              .format(user_item, computer_item, result))
        return result
