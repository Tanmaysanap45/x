from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#training data
text = [
    "I like Criket",
    "Football is my fav sport",
    "I watch criket matches",
    "I Like Studying Computer science",
    "Python is easy to learn",
    "I study mathematics"
  ]

#categories
category = [
    "sports",
    "sports",
    "sports",
    "Education",
    "Education",
    "Education"
]

#covert text into numbers
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(text)

#create and train the model
model = MultinomialNB()
model.fit(x,category)

#input
sentence = input("Enter a sentence: ")

#convert input in numbers
sentence_vector = vectorizer.transform([sentence])

#Check whether any known word is present
if sentence_vector.nnz == 0:
  print("not trained for this data")
else:
  result = model.predict(sentence_vector)
  print("Predicted Category:", result[0])
