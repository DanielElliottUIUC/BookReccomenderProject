import pandas as pd
print("working")
df = pd.read_csv("books_data.csv")
df_new = df.drop(df.columns[2:], axis =1)
df_cleaned = df_new.dropna()
print(df_cleaned.head(10))
df_cleaned.to_csv("books_data_cleaned.csv", index=False)
print("File saved")