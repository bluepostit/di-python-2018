import json

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


def show_menu():
    menu = """
    MENU
 (s) Search for words
 (r) View last search results
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
                matches = search(search_text)
                # Store it in last_search
                last_search['search_text'] = search_text
                last_search['matches'] = matches
                show_results(search_text, matches)
        elif choice == 'r':
            if last_search == {}:
                print("No search results yet.")
            else:
                show_results(last_search['search_text'],
                             last_search['matches'])
        choice = input(menu).strip().lower()


def show_results(search_text, matches):
    print(f"You searched for \"{search_text}\"")
    if len(matches) < 1:
        print("I found no matches for this word.")
    else:
        print(f"I found {len(matches)} words that match:")
        for i, match in enumerate(matches):
            print(f" {i + 1:3}. {match}")


def test():
    text = input("Text to search for: ")
    matches = search(text)
    print("Matches: ")
    print("\n".join(matches))
    save_search(text, matches)

def test2():
    text = 'yair'
    matches = search(text)
    show_results(text, matches)

#test2()
show_menu()