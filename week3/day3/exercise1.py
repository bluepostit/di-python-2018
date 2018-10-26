import json

WORD_LIST_PATH = '../sowpods.txt'
LAST_SEARCH_PATH = 'last_search.json'


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


def test():
    text = input("Text to search for: ")
    matches = search(text)
    print("Matches: ")
    print("\n".join(matches))
    save_search(text, matches)

test()