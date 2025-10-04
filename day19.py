#NumPy is a library for numerical & mathematical operations. It is extremely fast compared to Python lists because it uses C language implementation under the hood.
#Pandas is built on top of NumPy. It’s used for data handling, cleaning, and analysis, especially tabular data (like Excel or CSV).

# import numpy as np
import pandas as pd
# arr=np.array([1,3,4,6,7,89,3,4,5,5,5,555,5])
# print(arr.mean())
# print(arr+6)

# matrix=np.array([[1,3],[12,4]])
# print(matrix)

# data=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
# print(data)

data={
    "Name":["Asad","Waqas","Ali"],
    "Age":[23,25,22],
    "City":["Kasur","Khudian","Lahore"]
}
df=pd.DataFrame(data)
# print(df)
# df=pd.read_csv("expanses.csv")
# print(df.head())
# #print(df.head())       # Show first 5 rows
# print(df.tail())       # Show last 5 rows
# print(df.shape)        # Rows and columns
# print(df.columns)      # Column names
# print(df.info())       # Data types
# print(df.describe())   # Summary (mean, std, etc.)
# Selecting a column
# print(df["Name"])

# # Selecting multiple columns
# print(df[["Name", "Age"]])

# # Selecting rows
# print(df.iloc[0])   # First row
# print(df.loc[1])    # Row with index 1
# Filter rows where Age > 23
# print(df[df["Age"] > 23])
# Sort by Age
print(df.sort_values("Age"))



