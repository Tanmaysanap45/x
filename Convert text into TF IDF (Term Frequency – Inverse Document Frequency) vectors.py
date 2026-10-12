from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "Students study Python programming",
    "Python is easy to learn",
    "Programming improves problem solving"
    ]
vector = TfidfVectorizer()
tfid_matrix = vector.fit_transform(documents)

df = pd.DataFrame(
    tfid_matrix.toarray(),
    columns = vector.get_feature_names_out(),
    index = ["D1" , "D2" , "D3"]
    )
print(df.round(2))
