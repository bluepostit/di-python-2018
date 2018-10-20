from game import Game


def get_user_menu_choice():
    menu = """\
    Menu:
    (g) Play a new game
    (x) Show scores and exit
     :  """
    choice = input(menu).strip().lower()
    return choice


def print_results(results):
    total_games = len(results)
    wins = len([r for r in results if r == 'win'])
    draws = len([r for r in results if r == 'draw'])
    losses = total_games - wins - draws
    print(f""" \
    Game Results:
      You won {wins} times
      You lost {losses} times
      You drew {draws} times

    Thank you for playing!
    """)


def main():
    results = []
    user_choice = get_user_menu_choice()
    while user_choice != 'x':
        if user_choice == 'g':
            game = Game()
            result = game.play()
            results.append(result)
        elif user_choice != 'x':
            print("Invalid choice. Please try again")
        user_choice = get_user_menu_choice()
    print_results(results)

main()
