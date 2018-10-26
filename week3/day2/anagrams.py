from anagram_checker import AnagramChecker


class Anagrams:
    def __init__(self):
        self.checker = AnagramChecker()

    def get_menu_selection(self):
        menu = """\
    \n\tAnagram Checker
    (w) Look up anagrams for a word
    (x) Exit
     : """
        choice = input(menu).strip().lower()
        return choice

    def get_user_word(self):
        word = input("Please type a single word: ").strip()
        # Did the user type more than one word?
        word_count = len(word.split())
        if word_count > 1:
            print("You must enter one word only.")
            return None
        # Did the user enter only alphabetic characters?
        elif not word.isalpha():
            print("You must enter one or more alphabetic characters.")
            return None
        else:
            return word

    def get_is_valid_word(self, word):
        return self.checker.is_valid_word(word)

    def get_anagrams(self, word):
        return self.checker.get_anagrams(word)

    def show_info(self, word, is_valid_word, anagrams):
        print()
        print('-' * 40)
        print(f"Your word: '{word}'.")
        if is_valid_word:
            print("This is a valid English word.")
        else:
            print("This is not a valid English word.")
        if len(anagrams) == 0:
            print("There are no anagrams for your word.")
        else:
            print(f"Anagrams for your word: {', '.join(anagrams)}")
        print('-' * 40)
        print()


def main():
    ana = Anagrams()
    choice = ana.get_menu_selection()
    while choice != 'x':
        if choice == 'w':
            word = ana.get_user_word()
            if word is not None:
                is_valid_word = ana.get_is_valid_word(word)
                anagrams = ana.get_anagrams(word)
                ana.show_info(word, is_valid_word, anagrams)
        else:
            print("Please choose from the menu.")
        choice = ana.get_menu_selection()


main()

