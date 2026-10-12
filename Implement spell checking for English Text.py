from spellchecker import SpellChecker

spell = SpellChecker()
sentence = input("Enter a sentence: ")
words = sentence.split()
corrected = []

for word in words:
    correct_word = spell.correction(word)
    
    if correct_word is None:
        corrected.append(word)
    else:
        corrected.append(correct_word)

print("\nOriginal Sentence:")
print(sentence)
print("\nCorrected Sentence:")
print(" ".join(corrected))
