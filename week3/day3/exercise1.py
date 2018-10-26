import json
import os.path as path

WORD_LIST_PATH = '../sowpods.txt'
LAST_SEARCH_PATH = 'last_search.json'

last_search = {}


def read_word_list():
    with open(WORD_LIST_PATH) as f:
        words = [line.strip().lower()
                 for line in f.readlines()]
        return words


def search(text):
    text = text.strip().lower()
    words = read_word_list()
    matches = []
    for word in words:
        if text in word:
            matches.append(word)
    return matches


def save_search(text, results):
    search_as_dict = {
        "search_text": text,
        "results": results
    }
    with open(LAST_SEARCH_PATH, 'w') as f:
        json.dump(search_as_dict, f, indent=4)


def get_shortest_word(word_list):
    shortest = None
    shortest_length = 100
    for word in word_list:
        word_length = len(word)
        if word_length < shortest_length:
            shortest = word
            shortest_length = word_length
    return shortest


def get_longest_word(word_list):
    longest = None
    longest_length = 1
    for word in word_list:
        word_length = len(word)
        if word_length > longest_length:
            longest = word
            longest_length = word_length
    return longest


def get_average_word_length(word_list):
    lengths = [len(word) for word in word_list]
    total = sum(lengths)
    average = total / len(word_list)
    return average


def show_statistics():
    words = read_word_list()

    shortest = get_shortest_word(words)
    longest = get_longest_word(words)
    average = get_average_word_length(words)

    print("\tINFORMATION")
    print(f"There are {len(words)} words in the list")
    print(f"The shortest word is '{shortest}' ({len(shortest)})")
    print(f"The longest word is '{longest}' ({len(longest)})")
    print(f"Average word length is {average:2.2} characters")


def show_menu():
    menu = """
    MENU
 (s) Search for words
 (r) View last search results
 (i) Information about the word list
 (x) Exit
  : """
    choice = input(menu).strip().lower()
    while choice != 'x':
        if choice == 's':
            search_text = input(
                "Please type a pattern to search for: ").strip()
            # Did the user enter only alphabetic characters?
            if not search_text.isalpha():
                print("You must enter one or more "
                      "alphabetic characters.")
            else:
                results = search(search_text)
                # Store it in last_search
                last_search['search_text'] = search_text
                last_search['results'] = results
                # Save it to the JSON file
                save_search(search_text, results)
                show_results(search_text, results)
        elif choice == 'r':
            if last_search == {}:
                print("No search results yet.")
            else:
                show_results(last_search['search_text'],
                             last_search['results'])
        elif choice == 'i':
            show_statistics()
        choice = input(menu).strip().lower()


def show_results(search_text, matches):
    print(f"You searched for \"{search_text}\"")
    if len(matches) < 1:
        print("I found no matches for this word.")
    else:
        print(f"I found {len(matches)} words that match:")
        for i, match in enumerate(matches):
            print(f" {i + 1:3}. {match}")


# First, check if the LAST_SEARCH_PATH file exists.
if path.exists(LAST_SEARCH_PATH):
    # Load it with json, and store it in the last_search variable
    with open(LAST_SEARCH_PATH) as f:
        last_search = json.load(f)
# Show the menu, even if the file does not exist.
show_menu()