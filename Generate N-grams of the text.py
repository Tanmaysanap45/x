import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
text = "Artificial intelligence is changing the way people work and communicate every day."
tokens = word_tokenize(text.lower())

trigrams = list (ngrams (tokens, 2))

print("Generated Trigrams:")
for trigram in trigrams:
    print(trigram)

trigram_freq = Counter(trigrams)
print("\nTrigram Frequencies:")
for trigram, freq in trigram_freq.items():
    print(f"{trigram}: {freq}")
