import nltk
import io
import base64
from matplotlib import pyplot as plt
import numpy as np
import IPython.display as display
from nltk.chunk import RegexpParser
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
grammar_pattern = r"""
NP: {<DT>?<JJ>*<NN>}
VP: {<VB.*><NP|PP|CLAUSE>+$}
PP: {<IN><NP>}
CLAUSE: {<NP><VP>}
"""
s = "The quick brown fox jumped over the lazy dog."
tokens = nltk.word_tokenize(s)
pos_tags = nltk.pos_tag(tokens)
parser = RegexpParser(grammar_pattern)
tree = parser.parse(pos_tags)
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print(' '.join(word for word, tag in subtree.leaves()))
