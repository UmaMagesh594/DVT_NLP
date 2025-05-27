import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
sentence = "the quick brown fox jumps over the lazy dog."
words = word_tokenize(sentence)
morph = nltk.PorterStemmer()
stemmed_words = [morph.stem(word) for word in words]
print("Original Text: ",sentence)
print("Tokenized Words: ",words)
print("Stemmed_words: ",stemmed_words)
