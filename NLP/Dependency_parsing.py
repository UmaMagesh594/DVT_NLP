import spacy
from spacy import displacy
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
sentence = "The autonomous robot efficiently navigates through obstacles."

doc = nlp(sentence)
print("Token\t\tDependency\t\tHead")
print("="*40)
for token in doc:
  print(f"{token.text}\t\t{token.dep_}\t\t{token.head.text}")
displacy.serve(doc, style="dep")
