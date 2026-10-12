import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The teacher explained the lessons while the students were listening carefully."
tokens = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Stemming:")
for word in tokens:
    print(f"{word} -> {stemmer.stem(word)}")

print("\nLemmatization:")
for word in tokens:
    print(f"{word} -> {lemmatizer.lemmatize(word)}")
