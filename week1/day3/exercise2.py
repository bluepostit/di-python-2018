paragraph = '''
Tree frogs are usually tiny as their weight has to be carried 
by the branches and twigs in their habitats. While some reach 
10 cm (4 in) or more, they are typically smaller and more slender 
than terrestrial frogs. Tree frogs typically have well-developed 
discs at the finger and toe tips; the fingers and toes themselves, 
as well as the limbs, tend to be rather small, resulting in a 
superior grasping ability. The genus Chiromantis of the 
Rhacophoridae is most extreme in this respect: it can oppose two 
fingers to the other two, resulting in a vise-like grip.'''.strip()

sentences = paragraph.strip().split('. ')
words = paragraph.split(' ')
unique_words = set(words)

# 2.4 - non-whitespace characters
# compare str.isspace() to str.isnumeric()
non_whitespace_chars = [char for char in paragraph if not char.isspace()]


print("The paragraph has {} sentences".format(len(sentences)))
print("The paragraph has {} words".format(len(words)))
print("The paragraph has {} unique words".format(len(unique_words)))
print("The paragraph has {} non-unique words".format(
    len(words) - len(unique_words)))
print("The paragraph has {} characters".format(len(paragraph)))
print("The paragraph has {} non-whitespace characters".format(
    len(non_whitespace_chars)))
