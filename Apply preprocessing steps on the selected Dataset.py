import pandas as pd
df=pd.read_csv("amazon.csv")
print(df.head())

print("Original Dataset:")
print(df)

df=df.dropna()

df=df.drop_duplicates()

print("\n Cleaned Dataset:")
print(df)

df.to_csv("amazon_cleaned.csv", index=False)
print("\n Blank values and duplicate rows removed successfully.")
