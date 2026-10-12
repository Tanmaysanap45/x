import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is a fascinating field. It allows computers to understand human language."
#sentence segmentaion
sentences = sent_tokenize(text)
print("Sentence Segmentation: ")

for idx, sentence in enumerate(sentences, 1):
    print(f"{idx}: {sentence}")

print("\nWord Tokenization:")
for idx, sentence in enumerate(sentences,1):
    words = word_tokenize(sentence)
    print(f"{idx}: {words}")
