import random

WORD_LIST_FILE_PATH = '../sowpods.txt'


def get_words_from_file():
    with open(WORD_LIST_FILE_PATH, 'r') as f:
        words = [line.strip().lower() for line in f.readlines()]
        return words


def get_random_sentence(length):
    randoms = []
    words = get_words_from_file()
    for i in range(length):
        index = random.randint(0, len(words))
        rand_word = words[index]
        randoms.append(rand_word)
    return " ".join(randoms)


def main():
    info = """\
This program prints a sentence of random words.
You can choose the length of the sentence."""
    print(info)
    length_str = input("Please type a length between 2 and 20: ").strip()
    if not length_str.isdigit():
        print("You did not type a number. ")
        return
    # If we reach this point, we know that length is numeric.
    length = int(length_str)
    if (length < 2) or (length > 20):
        print("Length must be between 2 and 20!")
        return
    # If we reach this point, length is valid
    sentence = get_random_sentence(length)
    print(f"Your random sentence is: '{sentence}'")


# Test function to check that my functions work
def test():
    for i in range(10):
        sentence = get_random_sentence(i)
        print(sentence)


# test()
main()
