class AnagramChecker:
    def __init__(self):
        with open('../sowpods.txt') as f:
            self.words = [word.strip().lower()
                          for word in f.readlines()]

    def is_valid_word(self, word):
        return word.lower() in self.words

    def get_anagrams(self, word):
        anagrams = []
        # Get the word as a sorted list of letters,
        # eg. 'date' -> ['a', 'd', 'e', 't']
        word_sorted = sorted(word)
        for list_word in self.words:
            # Skip the word itself
            if list_word == word:
                continue
            list_word_sorted = sorted(list_word)
            # When the letters of each of the two words are sorted,
            # they match each other exactly.
            # This means that the words are anagrams of each other.
            if list_word_sorted == word_sorted:
                # Careful! We don't want to add the SORTED word,
                # but the original, unsorted word.
                anagrams.append(list_word)
        return anagrams
