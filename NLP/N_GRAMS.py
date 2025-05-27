from nltk.util import ngrams
s = "This My laptop it's very comfortable for me"
w = s.split()
bi_gram = list(ngrams(w,2))
tri_gram = list(ngrams(w,2))
print("BI-GRAM:",bi_gram)
print("TRI-GRAM:",tri_gram)
