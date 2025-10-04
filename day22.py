# Day 22: Matplotlib – Data Visualization
# ✅ What is Matplotlib?

# It’s Python’s most popular data visualization library.

# Used to create line plots, bar charts, histograms, scatter plots, pie charts, etc.

# Works very well with NumPy and Pandas.
import pandas as pd
import matplotlib.pyplot as plt

# x=[2,4,5,6,7,8]
# y=[23,56,8,5,1,45]
# plt.plot(x,y, marker="o")
# plt.title("Asad's Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()
###########################################33
df=pd.read_csv("sales.csv")
# sales_count=df.groupby("Product")["Sales"].sum()
# sales_count.plot(kind="bar",color="skyblue",edgecolor="black")
# plt.title("Sales Plot")
# plt.xlabel("Products")
# plt.ylabel("Sales")
# plt.show()
# region_sales = df.groupby("Region")["Sales"].sum()

# # Pie Chart
# region_sales.plot(kind="pie", autopct='%1.1f%%', startangle=90, colormap="Set3")
# plt.title("Sales Distribution by Region")
# plt.ylabel("")  # Hide Y label
# plt.show()
# Convert Date to datetime
# df["Date"] = pd.to_datetime(df["Date"])

# # Line Chart
# plt.plot(df["Date"], df["Sales"], marker="o", color="green")
# plt.title("Sales Over Time")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.show()
# plt.scatter(df["Product"], df["Sales"], color="red", s=100, alpha=0.7)
# plt.title("Sales per Product (Scatter Plot)")
# plt.xlabel("Product")
# plt.ylabel("Sales")
# plt.show()
import numpy as np

arr=np.array([1,2,56,77,89])
print(arr)
print(arr*3)


