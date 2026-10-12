import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Download required resources (run only once)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

print("pos Tags:")
print(pos_tags)

tags = [tag for word, tag in pos_tags]
tag_count = Counter(tags)

print("\nCount of POS Tags:")
for tag, count in tag_count.items():
    print(f"{tag} : {count}")
