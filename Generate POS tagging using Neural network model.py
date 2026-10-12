import spacy
nlp = spacy.load("en_core_web_sm")

text = "Artificial intelligence is changing the way people work and communicate every day."

doc = nlp(text)
print("\nPoS Tagging using Neural Model(SpaCy)")
for token in doc:
    print(f"{token.text} -> {token.pos_}({token.tag_})")
