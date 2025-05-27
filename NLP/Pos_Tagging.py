import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
sentence = "the quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
