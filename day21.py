# import pandas as pd

# data = {
#     "Name": ["Asad", "Ali", "Sara", "Asad", "Ali"],
#     "Subject": ["Math", "Math", "Math", "English", "English"],
#     "Marks": [85, 90, 88, 92, 80]
# }

# df = pd.DataFrame(data)
# mean_marks=df.groupby("Subject")["Marks"].mean()
# print(mean_marks)
# agg_marks=df.groupby("Subject")["Marks"].agg(["mean","sum","count"])
# print(agg_marks)
# student=pd.DataFrame({
#     "ID":[1,2,3],
#     "Names":["Asad","Waqas","Ali"]
# })
# score=pd.DataFrame({
#     "ID":[1,2,3],
#     "Marks":[98,95,93]
# })
# merged=pd.merge(student,score,on="ID")
# print(merged)

# df1 = pd.DataFrame({"Name": ["Asad", "Ali"], "Age": [23, 25]})
# df2 = pd.DataFrame({"Name": ["Sara", "Ahsan"], "Age": [22, 24]})

# df3 = pd.concat([df1, df2])
# print(df3)
# data = {"Name": ["Asad", "Ali", "Sara"], "Age": [23, None, 22]}
# df = pd.DataFrame(data)

# print(df)

# # Fill missing values
# print(df.fillna(0))

# # Drop rows with missing values
# print(df.dropna())
# df = pd.DataFrame({
#     "Name": ["Asad", "Ali", "Sara", "Asad"],
#     "Marks": [90, 85, 95, 88],
#     "Age": [23, 25, 22, 23]
# })

# # print(df.sort_values(["Age","Marks"],ascending=[True,False]))
# pivot = df.pivot_table(index="Name", values="Marks", aggfunc="mean")
# print(pivot)
####################################################
import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

print("📌 Original Data")
print(df)

# 1. Average marks of each student
print("\n📌 Average Marks of Students")
print(df.groupby("Name")["Marks"].mean())

# 2. Highest marks in each subject
print("\n📌 Highest Marks per Subject")
print(df.groupby("Subject")["Marks"].max())

# 3. Which student got the highest total marks?
print("\n📌 Total Marks per Student")
print(df.groupby("Name")["Marks"].sum())

# 4. Sort students by total marks (descending)
print("\n📌 Students Sorted by Total Marks")
print(df.groupby("Name")["Marks"].sum().sort_values(ascending=False))

# 5. Pivot Table – Subject wise average marks per student
print("\n📌 Pivot Table")
print(df.pivot_table(index="Name", columns="Subject", values="Marks", aggfunc="mean"))
import pandas as pd

# Load CSV
df = pd.read_csv("sales.csv")

print("📌 Sales Data:")
print(df.head())

# 1. Total sales
print("\n✅ Total Sales:", df["Sales"].sum())

# 2. Sales by Region
print("\n✅ Sales by Region:")
print(df.groupby("Region")["Sales"].sum())

# 3. Sales by Product
print("\n✅ Sales by Product:")
print(df.groupby("Product")["Sales"].sum())

# 4. Best-selling product
print("\n✅ Best Selling Product:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(1))

# 5. Average sales per transaction
print("\n✅ Average Sales per Transaction:", df["Sales"].mean())

# 6. Pivot Table → Product sales in each region
print("\n✅ Pivot Table - Product Sales by Region:")
print(df.pivot_table(index="Product", columns="Region", values="Sales", aggfunc="sum", fill_value=0))

# 7. Find the day with highest sales
print("\n✅ Day with Highest Sales:")
print(df.loc[df["Sales"].idxmax()])





