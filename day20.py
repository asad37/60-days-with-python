# 📅 Day 20: Pandas – Data Analysis Made Easy
# ✅ What is Pandas?

# Pandas is a Python library used for data manipulation and analysis.

# It provides fast, flexible, and expressive data structures like:

# Series → 1D labeled array (like a list with labels).

# DataFrame → 2D labeled data structure (like an Excel sheet or SQL table).

# 🔹 Installation
# pip install pandas

# 🔹 Importing Pandas
# import pandas as pd

# 1️⃣ Pandas Series (1D data)

# Think of it as a single column.

# import pandas as pd

# # Creating a Series
# s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
# print(s)


# 👉 Output:

# a    10
# b    20
# c    30
# d    40
# dtype: int64

# 2️⃣ Pandas DataFrame (2D data)

# Think of it like a full Excel table.

# data = {
#     "Name": ["Asad", "Ali", "Sara"],
#     "Age": [23, 25, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }

# df = pd.DataFrame(data)
# print(df)


# 👉 Output:

#    Name  Age       City
# 0  Asad   23     Lahore
# 1   Ali   25    Karachi
# 2  Sara   22  Islamabad

# 3️⃣ Reading and Writing Files with Pandas
# # Reading CSV file
# df = pd.read_csv("data.csv")

# # Writing to CSV
# df.to_csv("output.csv", index=False)

# # Reading Excel file
# df = pd.read_excel("data.xlsx")

# # Writing to Excel
# df.to_excel("output.xlsx", index=False)

# 4️⃣ Pandas Basic Operations
# print(df.head())       # Show first 5 rows
# print(df.tail())       # Show last 5 rows
# print(df.shape)        # Rows and columns
# print(df.columns)      # Column names
# print(df.info())       # Data types
# print(df.describe())   # Summary (mean, std, etc.)

# 5️⃣ Selecting Data
# # Selecting a column
# print(df["Name"])

# # Selecting multiple columns
# print(df[["Name", "Age"]])

# # Selecting rows
# print(df.iloc[0])   # First row
# print(df.loc[1])    # Row with index 1

# 6️⃣ Filtering Data
# # Filter rows where Age > 23
# print(df[df["Age"] > 23])

# 7️⃣ Adding New Column
# df["Score"] = [90, 85, 95]
# print(df)

# 8️⃣ Sorting Data
# # Sort by Age
# print(df.sort_values("Age"))

# 📌 Summary of Today

# Pandas is powerful for data analysis.

# We learned about Series, DataFrame, reading/writing files, selecting & filtering data, adding columns, sorting.